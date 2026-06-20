class ConditionEvaluator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def evaluate(self):
        return self.x > 5 and self.y < 10

if __name__ == '__main__':
    evaluator = ConditionEvaluator(6, 8)
    result = evaluator.evaluate()
    print(result)