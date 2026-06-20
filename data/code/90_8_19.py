class BooleanEvaluator:
    def evaluate(self, a, b):
        return (a > 5) or (b < 10)

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result1 = evaluator.evaluate(6, 7)
    result2 = evaluator.evaluate(4, 11)
    print(f"Result for a=6, b=7: {result1}")
    print(f"Result for a=4, b=11: {result2}")