import os
from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="Todd Phillips")
    d2 = Director(id=2, name="Quentin Tarantino")
    d3 = Director(id=3, name="Chad Stahelski")
    d4 = Director(id=4, name="Benny Safdie")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3, d4])
    director_dao.create = MagicMock(return_value=Director(id=4))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {"id": 5, "name": "Vasyatest Pupkintest"}
        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_update(self):
        self.director_service.delete(1)

    def test_delete(self):
        director_d = {"id": 5, "name": "Vasyatest Pupkintest"}
        self.director_service.update(director_d)


if __name__ == '__main__':
    os.system("pytest")
