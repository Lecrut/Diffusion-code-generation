import random

class NumberChecker:
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    @staticmethod
    def check_even_odd(number):
        if number % 2 == 0:
            print('Even')
        else:
            print('Odd')

if __name__ == '__main__':
    checker = NumberChecker()
    for _ in range(10):
        random_number = random.randint(NumberChecker.MIN_NUMBER, NumberChecker.MAX_NUMBER)
        checker.check_even_odd(random_number)