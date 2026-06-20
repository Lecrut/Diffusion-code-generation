class NumberChecker:

    @staticmethod
    def is_odd(n):
        return bool(n & 1)
if __name__ == '__main__':
    value1 = 7
    value2 = 8
    print(NumberChecker.is_odd(value1))
    print(NumberChecker.is_odd(value2))