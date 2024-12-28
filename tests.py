import pytest
from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book(self, collector):
        collector.add_new_book("451 градус по Фаренгейту")
        assert "451 градус по Фаренгейту" in collector.get_books_genre()

    def test_add_new_book_invalid_length(self, collector):
        collector.add_new_book("")  # слишком короткое имя
        collector.add_new_book("К" * 42)  # слишком длинное имя
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self, collector):
        collector.add_new_book("Братство кольца")
        collector.set_book_genre("Братство кольца", "Фантастика")
        assert collector.get_book_genre("Братство кольца") == "Фантастика"

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book("Волшебник Изумрудного города")
        collector.set_book_genre("Волшебник Изумрудного города", "Роман")
        assert collector.get_book_genre("Волшебник Изумрудного города") == ""

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Ужасы")
        assert collector.get_books_with_specific_genre("Ужасы") == ["Мастер и Маргарита"]

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Колобок")
        collector.set_book_genre("Колобок", "Мультфильмы")
        assert "Колобок" in collector.get_books_for_children()

    def test_get_books_for_children_age_rating(self, collector):
        collector.add_new_book("Портрет Дориана Грея")
        collector.set_book_genre("Портрет Дориана Грея", "Ужасы")
        assert "Портрет Дориана Грея" not in collector.get_books_for_children()

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Этюд в багровых тонах")
        collector.add_book_in_favorites("Этюд в багровых тонах")
        assert "Этюд в багровых тонах" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Анна Каренина")
        collector.add_book_in_favorites("Анна Каренина")
        collector.delete_book_from_favorites("Анна Каренина")
        assert "Анна Каренина" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []