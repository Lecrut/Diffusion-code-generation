class TruthyEvaluator:
    def __init__(self, items):
        self.items = items

    def is_any_truthy(self):
        return any(self.items)

if __name__ == '__main__':
    evaluator = TruthyEvaluator([0, 0, 1])
    print(evaluator.is_any_truthy())
    evaluator2 = TruthyEvaluator([False, None, 0])
    print(evaluator2.is_any_truthy())