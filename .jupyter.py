{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "19613b3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "832a4b1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies = pd.read_csv('tmdb_5000_movies.csv')\n",
    "credits = pd.read_csv('tmdb_5000_credits.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "96acb238",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>genres</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>keywords</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>popularity</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>production_countries</th>\n",
       "      <th>release_date</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>spoken_languages</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>237000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>19995</td>\n",
       "      <td>[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...</td>\n",
       "      <td>en</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>150.437577</td>\n",
       "      <td>[{\"name\": \"Ingenious Film Partners\", \"id\": 289...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2009-12-10</td>\n",
       "      <td>2787965087</td>\n",
       "      <td>162.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...</td>\n",
       "      <td>Released</td>\n",
       "      <td>Enter the World of Pandora.</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>7.2</td>\n",
       "      <td>11800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      budget                                             genres  \\\n",
       "0  237000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "\n",
       "                      homepage     id  \\\n",
       "0  http://www.avatarmovie.com/  19995   \n",
       "\n",
       "                                            keywords original_language  \\\n",
       "0  [{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...                en   \n",
       "\n",
       "  original_title                                           overview  \\\n",
       "0         Avatar  In the 22nd century, a paraplegic Marine is di...   \n",
       "\n",
       "   popularity                               production_companies  \\\n",
       "0  150.437577  [{\"name\": \"Ingenious Film Partners\", \"id\": 289...   \n",
       "\n",
       "                                production_countries release_date     revenue  \\\n",
       "0  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2009-12-10  2787965087   \n",
       "\n",
       "   runtime                                   spoken_languages    status  \\\n",
       "0    162.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...  Released   \n",
       "\n",
       "                       tagline   title  vote_average  vote_count  \n",
       "0  Enter the World of Pandora.  Avatar           7.2       11800  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f74503c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movie_id</th>\n",
       "      <th>title</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>[{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...</td>\n",
       "      <td>[{\"credit_id\": \"52fe48009251416c750aca23\", \"de...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movie_id   title                                               cast  \\\n",
       "0     19995  Avatar  [{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...   \n",
       "\n",
       "                                                crew  \n",
       "0  [{\"credit_id\": \"52fe48009251416c750aca23\", \"de...  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "credits.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "ab3e1035",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies = movies.merge(credits,on='title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1a645804",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>budget</th>\n",
       "      <th>genres</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>keywords</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>popularity</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>production_countries</th>\n",
       "      <th>release_date</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>spoken_languages</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>237000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>19995</td>\n",
       "      <td>[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...</td>\n",
       "      <td>en</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>150.437577</td>\n",
       "      <td>[{\"name\": \"Ingenious Film Partners\", \"id\": 289...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2009-12-10</td>\n",
       "      <td>2787965087</td>\n",
       "      <td>162.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...</td>\n",
       "      <td>Released</td>\n",
       "      <td>Enter the World of Pandora.</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>7.2</td>\n",
       "      <td>11800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      budget                                             genres  \\\n",
       "0  237000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "\n",
       "                      homepage     id  \\\n",
       "0  http://www.avatarmovie.com/  19995   \n",
       "\n",
       "                                            keywords original_language  \\\n",
       "0  [{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...                en   \n",
       "\n",
       "  original_title                                           overview  \\\n",
       "0         Avatar  In the 22nd century, a paraplegic Marine is di...   \n",
       "\n",
       "   popularity                               production_companies  \\\n",
       "0  150.437577  [{\"name\": \"Ingenious Film Partners\", \"id\": 289...   \n",
       "\n",
       "                                production_countries release_date     revenue  \\\n",
       "0  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2009-12-10  2787965087   \n",
       "\n",
       "   runtime                                   spoken_languages    status  \\\n",
       "0    162.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...  Released   \n",
       "\n",
       "                       tagline   title  vote_average  vote_count  \n",
       "0  Enter the World of Pandora.  Avatar           7.2       11800  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "f267dc10",
   "metadata": {},
   "outputs": [],
   "source": [
    "# genres\n",
    "#id\n",
    "#keywords\n",
    "#title\n",
    "#overview\n",
    "#cast \n",
    "#crew\n",
    "\n",
    "movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "b136c2fe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "en    7060\n",
       "ko     522\n",
       "fr      70\n",
       "es      32\n",
       "zh      27\n",
       "de      27\n",
       "hi      19\n",
       "ja      16\n",
       "it      14\n",
       "cn      12\n",
       "ru      11\n",
       "pt       9\n",
       "da       7\n",
       "sv       5\n",
       "nl       4\n",
       "fa       4\n",
       "th       3\n",
       "he       3\n",
       "ta       2\n",
       "cs       2\n",
       "ro       2\n",
       "id       2\n",
       "ar       2\n",
       "vi       1\n",
       "sl       1\n",
       "ps       1\n",
       "no       1\n",
       "ky       1\n",
       "hu       1\n",
       "pl       1\n",
       "af       1\n",
       "nb       1\n",
       "tr       1\n",
       "is       1\n",
       "xx       1\n",
       "te       1\n",
       "el       1\n",
       "Name: original_language, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies['original_language'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "fb6d01fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 7869 entries, 0 to 7868\n",
      "Data columns (total 47 columns):\n",
      " #   Column                Non-Null Count  Dtype  \n",
      "---  ------                --------------  -----  \n",
      " 0   budget                7869 non-null   int64  \n",
      " 1   genres                7869 non-null   object \n",
      " 2   homepage              2223 non-null   object \n",
      " 3   id                    7869 non-null   int64  \n",
      " 4   keywords              7869 non-null   object \n",
      " 5   original_language     7869 non-null   object \n",
      " 6   original_title        7869 non-null   object \n",
      " 7   overview              7866 non-null   object \n",
      " 8   popularity            7869 non-null   float64\n",
      " 9   production_companies  7869 non-null   object \n",
      " 10  production_countries  7869 non-null   object \n",
      " 11  release_date          7868 non-null   object \n",
      " 12  revenue               7869 non-null   int64  \n",
      " 13  runtime               7867 non-null   float64\n",
      " 14  spoken_languages      7869 non-null   object \n",
      " 15  status                7869 non-null   object \n",
      " 16  tagline               7025 non-null   object \n",
      " 17  title                 7869 non-null   object \n",
      " 18  vote_average          7869 non-null   float64\n",
      " 19  vote_count            7869 non-null   int64  \n",
      " 20  movie_id_x            7869 non-null   int64  \n",
      " 21  cast_x                7869 non-null   object \n",
      " 22  crew_x                7869 non-null   object \n",
      " 23  movie_id_y            7869 non-null   int64  \n",
      " 24  cast_y                7869 non-null   object \n",
      " 25  crew_y                7869 non-null   object \n",
      " 26  movie_id_x            7869 non-null   int64  \n",
      " 27  cast_x                7869 non-null   object \n",
      " 28  crew_x                7869 non-null   object \n",
      " 29  movie_id_y            7869 non-null   int64  \n",
      " 30  cast_y                7869 non-null   object \n",
      " 31  crew_y                7869 non-null   object \n",
      " 32  movie_id_x            7869 non-null   int64  \n",
      " 33  cast_x                7869 non-null   object \n",
      " 34  crew_x                7869 non-null   object \n",
      " 35  movie_id_y            7869 non-null   int64  \n",
      " 36  cast_y                7869 non-null   object \n",
      " 37  crew_y                7869 non-null   object \n",
      " 38  movie_id_x            7869 non-null   int64  \n",
      " 39  cast_x                7869 non-null   object \n",
      " 40  crew_x                7869 non-null   object \n",
      " 41  movie_id_y            7869 non-null   int64  \n",
      " 42  cast_y                7869 non-null   object \n",
      " 43  crew_y                7869 non-null   object \n",
      " 44  movie_id              7869 non-null   int64  \n",
      " 45  cast                  7869 non-null   object \n",
      " 46  crew                  7869 non-null   object \n",
      "dtypes: float64(3), int64(13), object(31)\n",
      "memory usage: 2.9+ MB\n"
     ]
    }
   ],
   "source": [
    "movies.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "39aa0b13",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "1967f97d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>movie_id</th>\n",
       "      <th>title</th>\n",
       "      <th>overview</th>\n",
       "      <th>genres</th>\n",
       "      <th>keywords</th>\n",
       "      <th>cast</th>\n",
       "      <th>crew</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19995</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...</td>\n",
       "      <td>[{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...</td>\n",
       "      <td>[{\"credit_id\": \"52fe48009251416c750aca23\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>285</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>Captain Barbossa, long believed to be dead, ha...</td>\n",
       "      <td>[{\"id\": 12, \"name\": \"Adventure\"}, {\"id\": 14, \"...</td>\n",
       "      <td>[{\"id\": 270, \"name\": \"ocean\"}, {\"id\": 726, \"na...</td>\n",
       "      <td>[{\"cast_id\": 4, \"character\": \"Captain Jack Spa...</td>\n",
       "      <td>[{\"credit_id\": \"52fe4232c3a36847f800b579\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>206647</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>A cryptic message from Bond’s past sends him o...</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>[{\"id\": 470, \"name\": \"spy\"}, {\"id\": 818, \"name...</td>\n",
       "      <td>[{\"cast_id\": 1, \"character\": \"James Bond\", \"cr...</td>\n",
       "      <td>[{\"credit_id\": \"54805967c3a36829b5002c41\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>49026</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>Following the death of District Attorney Harve...</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 80, \"nam...</td>\n",
       "      <td>[{\"id\": 849, \"name\": \"dc comics\"}, {\"id\": 853,...</td>\n",
       "      <td>[{\"cast_id\": 2, \"character\": \"Bruce Wayne / Ba...</td>\n",
       "      <td>[{\"credit_id\": \"52fe4781c3a36847f81398c3\", \"de...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>49529</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>John Carter is a war-weary, former military ca...</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>[{\"id\": 818, \"name\": \"based on novel\"}, {\"id\":...</td>\n",
       "      <td>[{\"cast_id\": 5, \"character\": \"John Carter\", \"c...</td>\n",
       "      <td>[{\"credit_id\": \"52fe479ac3a36847f813eaa3\", \"de...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   movie_id                                     title  \\\n",
       "0     19995                                    Avatar   \n",
       "1       285  Pirates of the Caribbean: At World's End   \n",
       "2    206647                                   Spectre   \n",
       "3     49026                     The Dark Knight Rises   \n",
       "4     49529                               John Carter   \n",
       "\n",
       "                                            overview  \\\n",
       "0  In the 22nd century, a paraplegic Marine is di...   \n",
       "1  Captain Barbossa, long believed to be dead, ha...   \n",
       "2  A cryptic message from Bond’s past sends him o...   \n",
       "3  Following the death of District Attorney Harve...   \n",
       "4  John Carter is a war-weary, former military ca...   \n",
       "\n",
       "                                              genres  \\\n",
       "0  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "1  [{\"id\": 12, \"name\": \"Adventure\"}, {\"id\": 14, \"...   \n",
       "2  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "3  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 80, \"nam...   \n",
       "4  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "\n",
       "                                            keywords  \\\n",
       "0  [{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...   \n",
       "1  [{\"id\": 270, \"name\": \"ocean\"}, {\"id\": 726, \"na...   \n",
       "2  [{\"id\": 470, \"name\": \"spy\"}, {\"id\": 818, \"name...   \n",
       "3  [{\"id\": 849, \"name\": \"dc comics\"}, {\"id\": 853,...   \n",
       "4  [{\"id\": 818, \"name\": \"based on novel\"}, {\"id\":...   \n",
       "\n",
       "                                                cast  \\\n",
       "0  [{\"cast_id\": 242, \"character\": \"Jake Sully\", \"...   \n",
       "1  [{\"cast_id\": 4, \"character\": \"Captain Jack Spa...   \n",
       "2  [{\"cast_id\": 1, \"character\": \"James Bond\", \"cr...   \n",
       "3  [{\"cast_id\": 2, \"character\": \"Bruce Wayne / Ba...   \n",
       "4  [{\"cast_id\": 5, \"character\": \"John Carter\", \"c...   \n",
       "\n",
       "                                                crew  \n",
       "0  [{\"credit_id\": \"52fe48009251416c750aca23\", \"de...  \n",
       "1  [{\"credit_id\": \"52fe4232c3a36847f800b579\", \"de...  \n",
       "2  [{\"credit_id\": \"54805967c3a36829b5002c41\", \"de...  \n",
       "3  [{\"credit_id\": \"52fe4781c3a36847f81398c3\", \"de...  \n",
       "4  [{\"credit_id\": \"52fe479ac3a36847f813eaa3\", \"de...  "
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54460030",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}