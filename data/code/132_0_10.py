class LogicEvaluator:
    @staticmethod
    def evaluate_logic(a, b):
        return a & b

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    print(evaluator.evaluate_logic(True, False))
    print(evaluator.evaluate_logic(False, True))
    print(evaluator.evaluate_logic(True, True))
    print(evaluator.evaluate_logic(False, False))