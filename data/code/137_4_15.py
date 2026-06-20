class BooleanEvaluator:
    def evaluate_and(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    result = evaluator.evaluate_and(True, True)
    print(result)