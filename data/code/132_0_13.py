class LogicEvaluator:
    def evaluate_logic(self, a, b):
        return a & b

if __name__ == '__main__':
    evaluator = LogicEvaluator()
    result1 = evaluator.evaluate_logic(True, False)
    result2 = evaluator.evaluate_logic(False, True)
    result3 = evaluator.evaluate_logic(True, True)
    print(result1, result2, result3)