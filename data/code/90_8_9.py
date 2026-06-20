class BooleanEvaluator:
    def evaluate_expression(self, a, b):
        return (a > 5) or (b < 10)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result1 = evaluator.evaluate_expression(6, 7)
    print(f"Result 1: {result1}")
    result2 = evaluator.evaluate_expression(3, 9)
    print(f"Result 2: {result2}")
    result3 = evaluator.evaluate_expression(4, 10)
    print(f"Result 3: {result3}")