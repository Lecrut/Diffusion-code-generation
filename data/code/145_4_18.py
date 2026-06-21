class StatusEvaluator:

    def __init__(self):
        self.thresholds = {'low': 30, 'medium': 60, 'high': 90}

    def evaluate(self, value):
        return 'Low' if value < self.thresholds['low'] else 'Medium' if value < self.thresholds['medium'] else 'High'
if __name__ == '__main__':
    evaluator = StatusEvaluator()
    print(evaluator.evaluate(25))
    print(evaluator.evaluate(45))
    print(evaluator.evaluate(75))