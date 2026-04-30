from datetime import datetime

from db.models import MovieSession
from django.shortcuts import get_object_or_404


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return movie_session


def get_movies_sessions(session_date: datetime = None) -> list:

    sessionset = MovieSession.objects.all()

    if session_date:
        return sessionset.filter(
            show_time__date=datetime.strptime(session_date, "%Y-%m-%d").date()
        )
    return sessionset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return get_object_or_404(MovieSession, id=movie_session_id)


def update_movie_session(session_id: int, *args, **kwargs) -> MovieSession:
    movie_session = (MovieSession.objects.filter(id=session_id)
                     .update(*args, **kwargs))
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
