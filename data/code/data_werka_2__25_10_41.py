class ZeroEvaluator:

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value == 0
if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '0', [], {}]
    evaluator = ZeroEvaluator(0)
    print(f'Is zero: {evaluator.evaluate()}')
    for value in sample_values:
        evaluator.value = value
        print(f'Value: {value}, Is zero: {evaluator.evaluate()}')