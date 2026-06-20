class ConditionEvaluator:
    def evaluate_and(self, a, b):
        return a and b

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    result = evaluator.evaluate_and(True, True)
    print(result)