class NumberComparator:

    @staticmethod
    def is_greater(a, b):
        return a > b
if __name__ == '__main__':
    print(NumberComparator.is_greater(10, 5))
    print(NumberComparator.is_greater(3, 7))
    print(NumberComparator.is_greater(8, 8))
    print(NumberComparator.is_greater(-1, -2))
    print(NumberComparator.is_greater(7, 7))