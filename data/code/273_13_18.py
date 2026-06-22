import random

class NumberEvaluator:
    COUNT = 10

    @staticmethod
    def check_even_odd():
        number = random.randint(1, 100)
        if number % 2 == 0:
            print('Even')
        else:
            print('Odd')

if __name__ == '__main__':
    for _ in range(NumberEvaluator.COUNT):
        NumberEvaluator.check_even_odd()