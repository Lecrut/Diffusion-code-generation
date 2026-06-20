class NumberEvaluator:
    def is_zero(self, number):
        return abs(number) < 1e-9

if __name__ == '__main__':
    evaluator = NumberEvaluator()
    print(f"is_zero(0): {evaluator.is_zero(0)}")
    print(f"is_zero(5): {evaluator.is_zero(5)}")
    print(f"is_zero(-0): {evaluator.is_zero(-0)}")
    print(f"is_zero(3.14): {evaluator.is_zero(3.14)}")