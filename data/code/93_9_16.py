class BooleanEvaluator:
    def evaluate(self, x: bool, y: bool) -> bool:
        return not x and not y

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result1 = evaluator.evaluate(False, False)
    print(f"False, False -> {result1}")
    result2 = evaluator.evaluate(True, False)
    print(f"True, False -> {result2}")
    result3 = evaluator.evaluate(True, True)
    print(f"True, True -> {result3}")
    result4 = evaluator.evaluate(False, True)
    print(f"False, True -> {result4}")