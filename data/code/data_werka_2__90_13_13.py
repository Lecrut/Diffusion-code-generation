class GreaterThanTenEvaluator:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def evaluate(self):
        return self.first_value > 10 or self.second_value > 10

if __name__ == '__main__':
    evaluator = GreaterThanTenEvaluator(12, 5)
    print(evaluator.evaluate())
    evaluator.second_value = 15
    print(evaluator.evaluate())