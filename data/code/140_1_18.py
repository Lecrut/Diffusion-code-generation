class NumberChecker:

    @staticmethod
    def is_even(number):
        return number & 1 == 0
if __name__ == '__main__':
    checker = NumberChecker()
    print(checker.is_even(4))
    print(checker.is_even(5))