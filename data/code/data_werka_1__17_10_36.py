class NumberEvaluator:
    def __init__(self, n):
        self.n = n

    def is_even(self):
        return self.n % 2 == 0

if __name__ == '__main__':
    evaluator1 = NumberEvaluator(10)
    evaluator2 = NumberEvaluator(15)
    print(evaluator1.is_even())
    print(evaluator2.is_even())