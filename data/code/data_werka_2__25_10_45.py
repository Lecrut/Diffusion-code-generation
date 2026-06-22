class ZeroEvaluator:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2.5, None, '0', [], {}]
    evaluator = ZeroEvaluator(0)
    for value in sample_values:
        print(f"is_zero({value}): {evaluator.evaluate()}")