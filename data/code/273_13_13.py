import random

class NumberChecker:
    def check_even_odd(self):
        number = random.randint(1, 100)
        if number % 2 == 0:
            print('Even')
        else:
            print('Odd')

if __name__ == '__main__':
    checker = NumberChecker()
    for _ in range(10):
        checker.check_even_odd()