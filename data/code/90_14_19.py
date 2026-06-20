class ConditionEvaluator:
    def __init__(self):
        self.value1 = 7
        self.value2 = 15

    def evaluate_or_condition(self):
        return self.value1 > 10 or self.value2 > 10

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    result = evaluator.evaluate_or_condition()
    print(result)