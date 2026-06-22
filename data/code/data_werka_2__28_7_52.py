class NumberComparator:
    @staticmethod
    def is_larger(a, b):
        return a > b

if __name__ == '__main__':
    print(NumberComparator.is_larger(10, 5))
    print(NumberComparator.is_larger(3, 7))
    print(NumberComparator.is_larger(-1, -2))
    print(NumberComparator.is_larger(0, 0))