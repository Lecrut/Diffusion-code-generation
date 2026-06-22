def check_any_true(values):
    if not values:
        return False
    for val in values:
        if val:
            return True
    return False

class BooleanEvaluator:
    def __init__(self, data):
        self.data = data

    def has_true(self):
        return check_any_true(self.data)

    def count_true(self):
        return sum(1 for x in self.data if x)

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    result = check_any_true(sample_values)
    print(result)
    
    evaluator = BooleanEvaluator([False, False, False])
    print(evaluator.has_true())
    print(evaluator.count_true())
    
    evaluator_true = BooleanEvaluator([True, False])
    print(evaluator_true.has_true())
    print(evaluator_true.count_true())