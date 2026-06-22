class DualFalseEvaluator:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    def is_both_false(self):
        return not self.val1 and not self.val2
    def summary(self):
        return (not self.val1, not self.val2)
if __name__ == '__main__':
    evaluator = DualFalseEvaluator(0, None)
    print(evaluator.is_both_false())
    print(evaluator.summary())