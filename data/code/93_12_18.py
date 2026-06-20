class BooleanEvaluator:
    def check_booleans(self, x: bool, y: bool) -> bool:
        return not x and not y

if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    print(evaluator.check_booleans(False, False))
    print(evaluator.check_booleans(True, False))
    print(evaluator.check_booleans(False, True))
    print(evaluator.check_booleans(True, True))