class NumberChecker:
    @staticmethod
    def is_odd(n):
        return n & 1 == 1

if __name__ == '__main__':
    value = 5
    print(NumberChecker.is_odd(value))