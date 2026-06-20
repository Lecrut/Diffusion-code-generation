class NumberEvaluator:
    def is_even_and_positive(self, n):
        return n > 0 and not (n & 1)

if __name__ == '__main__':
    evaluator = NumberEvaluator()
    print(evaluator.is_even_and_positive(4))
    print(evaluator.is_even_and_positive(-2))
    print(evaluator.is_even_and_positive(0))
    print(evaluator.is_even_and_positive(3))