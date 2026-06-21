class ZeroEvaluator:
    def __init__(self, value):
        self.value = value

    def is_zero(self):
        return self.value == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '0', [], {}]
    for value in sample_values:
        evaluator = ZeroEvaluator(value)
        print(f"{value}: {evaluator.is_zero()}")