class ThresholdEvaluator:
    def __init__(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two

    def evaluate(self):
        return self.value_one > 10 or self.value_two > 10

    def get_values(self):
        return self.value_one, self.value_two

if __name__ == '__main__':
    evaluator = ThresholdEvaluator(5, 15)
    print(evaluator.evaluate())
    print(evaluator.get_values())