import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['Террариум', 'Лолита', 'Книзь Юсупов'])
    def test_add_new_book_from_title_and_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_get_books_for_children_with_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга для взрослых")
        collector.set_book_genre("Книга для взрослых", "Недетский жанр")
        children_books = collector.get_books_for_children()
        assert "Книга для взрослых" not in children_books

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Марсианин")
        collector.set_book_genre("Марсианин", "Фантастика")
        assert collector.get_book_genre("Марсианин") == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Чужие")
        collector.set_book_genre("Чужие", "Ужасы")
        assert "Чужие" in collector.get_books_with_specific_genre("Ужасы")

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Матрица")
        collector.set_book_genre("Матрица", "Фантастика")
        assert "Матрица" in collector.get_books_genre()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер и Философский камень")
        collector.add_book_in_favorites("Гарри Поттер и Философский камень")
        assert "Гарри Поттер и Философский камень" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер и Кубок огня")
        collector.add_book_in_favorites("Гарри Поттер и Кубок огня")
        collector.delete_book_from_favorites("Гарри Поттер и Кубок огня")
        assert "Гарри Поттер и Кубок огня" not in collector.get_list_of_favorites_books()

    def test_add_new_book_with_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book("Анна Каренина, очень длинное название для книги, которое превышает 40 символов")
        assert "Анна Каренина, очень длинное название для книги, которое превышает 40 символов" not in collector.books_genre

    def test_set_invalid_book_genre(self):
        collector = BooksCollector()
        collector.set_book_genre("Террариум", "Неизвестный Жанр")
        assert collector.get_book_genre("Террариум") is None

    def test_get_books_with_invalid_genre(self):
        collector = BooksCollector()
        assert len(collector.get_books_with_specific_genre("Неизвестный Жанр")) == 0