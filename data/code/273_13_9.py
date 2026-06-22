import random

class NumberChecker:
    def check_number(self):
        number = random.randint(1, 100)
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    for _ in range(10):
        print(checker.check_number())