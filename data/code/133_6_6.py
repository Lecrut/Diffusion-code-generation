class FlagEvaluator:
    def __init__(self, flags):
        self.flags = [bool(flag) for flag in flags]

    def evaluate_consistency(self):
        return all(self.flags)

if __name__ == '__main__':
    evaluator = FlagEvaluator([1, 0, 1, 1, 0])
    print(evaluator.evaluate_consistency())