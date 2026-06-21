class ConditionEvaluator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def evaluate(self):
        return (self.x > 10) and (self.y < 50)

if __name__ == '__main__':
    evaluator = ConditionEvaluator(18, 42)
    print(evaluator.evaluate())