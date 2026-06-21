class NumberComparator:
    @staticmethod
    def is_larger(num1, num2):
        return num1 > num2

if __name__ == '__main__':
    print(NumberComparator.is_larger(10, 5))
    print(NumberComparator.is_larger(3, 7))
    print(NumberComparator.is_larger(-1, -2))
    print(NumberComparator.is_larger(0, 0))
    print(NumberComparator.is_larger(5.5, 2))