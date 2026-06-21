class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def is_identical(cls, book1, book2):
        return cls.compare_books(book1, book2)

    @staticmethod
    def compare_books(book1, book2):
        if not isinstance(book1, Book) or not isinstance(book2, Book):
            raise ValueError('Both arguments must be instances of Book')
        return book1.title == book2.title and book1.author == book2.author
if __name__ == '__main__':
    book_a = Book('1984', 'George Orwell')
    book_b = Book('1984', 'George Orwell')
    book_c = Book('Brave New World', 'Aldous Huxley')
    print(Book.is_identical(book_a, book_b))
    print(Book.is_identical(book_a, book_c))