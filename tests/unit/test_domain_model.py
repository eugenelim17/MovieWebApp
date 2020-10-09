from datetime import date

from movie.domain.model import Movie, Genre, User, Review, add_review

import pytest



@pytest.fixture()
def movie():
    movie = Movie('Moana', 2016)
    movie.description = 'In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana\'s island, she answers the Ocean\'s call to seek out the Demigod to set things right.'
    return movie


@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


@pytest.fixture()
def genre():
    return Genre('Action')


def test_user_construction(user):
    assert user.username == 'dbowie'
    assert user.password == '1234567890'
    assert repr(user) == '<User dbowie 1234567890>'

    for review in user.reviews:
        # User should have an empty list of Reviews after construction.
        assert False


def test_movie_construction(movie):
    assert movie.id is None
    assert movie.release_year == 2016
    assert movie.title == 'Moana'
    assert movie.description == 'In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana\'s island, she answers the Ocean\'s call to seek out the Demigod to set things right.'

    assert movie.number_of_reviews == 0
    assert movie.number_of_genres == 0

    assert repr(movie) == '<Movie Moana, 2016>'


def test_movie_less_than_operator():
    movie_1 = Movie('Moana', 2016)

    movie_2 = Movie('Frozen', 2013)

    assert movie_1 > movie_2


def test_genre_construction(genre):
    assert genre.genre_name == 'Action'

    for movie in genre.genre_movies:
        assert False

    assert not genre.is_applied_to(Movie("", 0))


def test_make_review_establishes_relationships(movie, user):
    review_text = 'Cool movie!'
    rating = 0
    review = add_review(review_text, user, movie, rating)

    # Check that the User object knows about the Review.
    assert review in user.reviews

    # Check that the Review knows about the User.
    assert review.user is user

    # Check that Movie knows about the Review.
    assert review in movie.reviews

    # Check that the Review knows about the Movie.
    assert review.movie is movie






