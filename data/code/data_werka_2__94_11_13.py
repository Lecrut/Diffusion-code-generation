def check_any_true(values):
    return any(values)

class BooleanEvaluator:
    def __init__(self, data):
        self.data = data

    def has_true(self):
        return any(self.data)

    def count_true(self):
        return sum(1 for val in self.data if val)

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = check_any_true(sample_values)
    print(result)

    evaluator = BooleanEvaluator([False, False, False])
    print(evaluator.has_true())
    print(evaluator.count_true())

    evaluator_true = BooleanEvaluator([True, False, True])
    print(evaluator_true.has_true())
    print(evaluator_true.count_true())