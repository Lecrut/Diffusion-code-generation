class LogicEvaluator:
    def evaluate_logic(self, a: bool, b: bool) -> str:
        if a and not b:
            return 'Decision A'
        elif not a and b:
            return 'Decision B'
        else:
            return 'No Decision'

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate_logic(True, False))
    print(evaluator.evaluate_logic(False, True))
    print(evaluator.evaluate_logic(True, True))
    print(evaluator.evaluate_logic(False, False))