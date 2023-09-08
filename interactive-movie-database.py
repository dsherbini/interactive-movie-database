# PPHA 30535: Python Programming for Public Policy
# Spring 2023
# HW3: Interactive Movie Database
# Author: Danya Sherbini

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use i
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/rating/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase


from numpy import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}
    
    def add_movie(self, title, year, category, rating, num_stars):
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
        print(f'{title} ({year}) added to the database.')
    
    def what_to_watch(self, category = ''):
        # using try/except to catch the ValueError
        try: 
            movies_by_category = []
            if not category:
                choice = random.choice(self.titles)
            else:
                for title, values in self.movies.items():
                    value = values['category']
                    if value == category:
                        movies_by_category.append(title)
                choice = random.choice(movies_by_category) # selecting random movie by category, not full list
            movie = self.movies[choice]
            print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['rating']}-rated {movie['category']}, and was given {movie['stars']} stars.")
        except ValueError:
            print('Error: You need to add a movie to the database!')


# creating new class InteractiveMovieDatabase
class InteractiveMovieDatabase(MovieDataBase):
    
    # overwriting the add_movie method
    def add_movie(self, title = '', year = '', category = '', rating = '', num_stars = ''):
        if not title:
            title = input('Please add a title: ')
            if title == 'None' or title == 'NA':
                title = input('Title cannot be None or NA. Please add new title: ')
        try:
            if not year:
                year = int(input('Please add a year: '))
        except ValueError:
            year = input('Year must be an integer. Enter year again: ')
        if not category:
            category = input('Please add a category: ')
            if category == 'None' or category == 'NA':
                category = input('Category cannot be None or NA. Please add new title: ')
        if not rating:
            rating = input("Please add a rating: ")
            assert(rating == 'G' or rating == 'PG' or rating == 'PG-13' or rating == 'R' or rating == 'Not Rated'), 'Rating must be G, PG, PG-13, R, or Not Rated'
        if not num_stars:
            num_stars = int(input('Please add a number of stars: '))
            stars = [1, 2, 3, 4, 5]
            assert(num_stars in stars), 'Number of stars must be between 1 and 5'
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'rating':rating, 'stars':num_stars}
        print(f'{title} ({year}) added to the database.')

    # creating the movie_rankings method
    def movie_rankings(self):
        movie_list = []
        ranked_movies = sorted(self.movies.items(), key = lambda element: element[1]['stars'], reverse = True)
        for movie in ranked_movies:
            title = movie[0]
            movie_list.append(title)
        return movie_list

