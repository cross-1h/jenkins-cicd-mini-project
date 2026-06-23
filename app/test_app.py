"""Unit tests for the sample Flask app.

Run locally with:  pytest -v
These same tests run automatically in the Jenkins `Test` stage.
"""

from app import add,subtract, app


def test_add():
    assert add(2, 4) == 6
    assert add(-1, 1) == 0


def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_add_route():
    client = app.test_client()
    response = client.get("/add/4/5")
    assert response.status_code == 200
    assert response.get_json()["result"] == 9


def test_subtract():
    assert add(5, -2) == 3
    assert subtract(10, 4) == 6


def test_subtract_route():
    client = app.test_client()
    response = client.get("/subtract/10/4")
    assert response.status_code == 200
    assert response.get_json()["result"] == 6

