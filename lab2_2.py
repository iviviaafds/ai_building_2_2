class Book:
    def __init__(self, id_, name, pages):
        """
        Инициализация книги.
        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц.
        """
        self.id = id_
        self.name = name
        self.pages = pages


class Library:
    def __init__(self, books=None):
        """
        Инициализация библиотеки.
        :param books: Список книг (по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.
        :return: int
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги по её идентификатору.
        :param book_id: Идентификатор книги.
        :return: int
        :raises ValueError: Если книги с таким id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Пример использования
if __name__ == '__main__':
    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]

    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1