# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:51:00 2024

@author: julir
"""

import pandas

file = pandas.read_csv("movie_dataset.csv")

print(file)

print(file.info())

"""

#   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None
"""

print(file)

"""
calculate the mean 
"""

x=file["Revenue (Millions)"].mean()
print (x)
"""
82.95637614678898

"""

file["Revenue (Millions)"].fillna(x, inplace = True)

print(file)

x=file["Metascore"].mean()

file["Metascore"].fillna(x, inplace = True)

print (file)

movies= file 

print(movies) 

"""
question1
"""
highest_Rating = movies['Rating'].max()
 
print(f"highest_Rating in the 'Rating' column is: {highest_Rating}")

highest_Rating_row = movies[movies['Rating'] == movies['Rating'].max()]

movie_name_highest_Rating = highest_Rating_row['Title'].values[0]

highest_Rating = highest_Rating_row['Rating'].values[0]

print(f"The movie with the highest Rating is '{movie_name_highest_Rating}' with a Rating of {highest_Rating}")

"""
answer 1 
highest_Rating in the 'Rating' column is: 9.0
The movie with the highest Rating is 'The Dark Knight' with a Rating of 9.0
"""

"""
question 2
"""

average_revenue = movies['Revenue (Millions)'].mean()

print(f"The average revenue is: {average_revenue} million dollars")

"""
The average revenue is: 82.95637614678898 million dollars
"""

"""
question 3
"""
filtered_movies = movies[(movies['Year'] >= 2015) & (movies['Year'] <= 2017)]
average_revenue_filtered = filtered_movies['Revenue (Millions)'].mean()

print(f"The average revenue for movies released between 2015 and 2017 is: {average_revenue_filtered} million dollars")

"""
Answer 
The average revenue for movies released between 2015 and 2017 is: 68.06402328198025 million dollars
"""

"""
question 4
"""

count_2016 = movies['Year'].value_counts().get(2016, 0)

print(f"The number of occurrences of 2016 in the 'Year' column is: {count_2016}")

"""
answer 297
"""

"""
question 5
"""

count_nolan = (movies['Director'] == 'Christopher Nolan').sum()

print(f"The number of times Christopher Nolan appears in the 'Director' column is: {count_nolan}")

"""
answer 5 
"""

"""
question 6 
"""
count_at_least_eight = (movies['Rating'] >= 8).sum()

print(f"The number of rows with a Rating of at least 8 is: {count_at_least_eight}")

"""
The number of rows with a Rating of at least 8 is: 78
"""

"""
question 7
"""

nolan_movies = movies[movies['Director'] == 'Christopher Nolan']
median_rating_nolan = nolan_movies['Rating'].median()

print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan}")

"""
answer 
The median rating of movies directed by Christopher Nolan is: 8.6
"""

"""
question 8 
"""

average_rating_by_year = movies.groupby('Year')['Rating'].mean()

highest_average_rating_year = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f"The year with the highest average rating is {highest_average_rating_year} with an average rating of {highest_average_rating}")


"""
answer 
The year with the highest average rating is 2007 with an average rating of 7.133962264150944
"""

"""
question 9 
"""

movies_2006 = movies[movies['Year'] == 2006]
movies_2016 = movies[movies['Year'] == 2016]


num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)


percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")

"""
answer 
The percentage increase in the number of movies made between 2006 and 2016 is: 575.00%
"""

"""
question 10
"""

all_actors = ', '.join(movies['Actors'].dropna())


all_actors_list = [actor.strip() for actor in all_actors.split(',')]


most_common_actor = pandas.Series(all_actors_list).mode().values[0]

print(f"The most common actor in all movies is: {most_common_actor}")

"""
answer
The most common actor in all movies is: Mark Wahlberg
"""

""" 
question 11
"""

all_genres = ', '.join(movies['Genre'].dropna())


all_genres_list = [genre.strip() for genre in all_genres.split(',')]


num_unique_genres = len(set(all_genres_list))

print(f"The number of unique genres in the dataset is: {num_unique_genres}")

"""
answer 
The number of unique genres in the dataset is: 20
"""

"""
Question 12
"""

numerical_features = movies.select_dtypes(include='number')


correlation_matrix = numerical_features.corr()


print("Correlation Matrix:")
print(correlation_matrix)

"""
Correlation Matrix:
                        Rank      Year  ...  Revenue (Millions)  Metascore
Rank                1.000000 -0.261605  ...           -0.252996  -0.185159
Year               -0.261605  1.000000  ...           -0.117562  -0.076077
Runtime (Minutes)  -0.221739 -0.164900  ...            0.247834   0.202239
Rating             -0.219555 -0.211219  ...            0.189527   0.604723
Votes              -0.283876 -0.411904  ...            0.607941   0.318116
Revenue (Millions) -0.252996 -0.117562  ...            1.000000   0.132304
Metascore          -0.185159 -0.076077  ...            0.132304   1.000000

[7 rows x 7 columns]

"""
numerical_features = movies.select_dtypes(include='number')


correlation_matrix = numerical_features.corr()

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Correlation Matrix")
plt.show()




















