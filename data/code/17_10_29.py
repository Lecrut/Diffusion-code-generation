class NumberEvaluator:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

if __name__ == '__main__':
    print(NumberEvaluator.is_even(10))
    print(NumberEvaluator.is_even(3))