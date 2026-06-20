class NumberEvaluator:
    def __init__(self):
        self.numbers = [8, 12]

    def evaluate_or_condition(self):
        return any(num > 10 for num in self.numbers)

if __name__ == '__main__':
    evaluator = NumberEvaluator()
    result = evaluator.evaluate_or_condition()
    print(result)