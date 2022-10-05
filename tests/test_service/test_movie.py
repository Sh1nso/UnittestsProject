from unittest.mock import MagicMock
import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.model.director import Director
from service.movie import MovieService
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(id=1, title='Attack_of_Titan', description='Hello_world', trailer='url', year=2015, rating=1000)

    movie_2 = Movie(id=2, title='Attack_of_Titan2', description='Hello_world2', trailer='url2', year=2015, rating=1000)
    movie_3 = Movie(id=3, title='Attack_of_Titan3', description='Hello_world3', trailer='url3', year=2015, rating=1000)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=1, title='Attack_of_Titan4', description='Hello_world4',
                                                    trailer='url4', year=2015, rating=1000))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'title': 'Gwinblade23',
            'description': 'Hello_world23',
            'trailer': 'url23',
            'year': 2015,
            'rating': 1000
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        movie = self.movie_service.delete(2)
        assert movie is None

    def test_update(self):
        movie_d = {
            'id': 3,
            'title': 'Gwinblade',
            'description': 'Hello_world15',
            'trailer': 'url15',
            'year': 2015,
            'rating': 1000
        }
        movie = self.movie_service.update(movie_d)
        assert movie is not None
