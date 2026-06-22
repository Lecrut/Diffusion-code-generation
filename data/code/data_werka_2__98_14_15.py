class ConditionEvaluator:
    def __init__(self, threshold_low, threshold_high, equality_target):
        self.threshold_low = threshold_low
        self.threshold_high = threshold_high
        self.equality_target = equality_target

    def evaluate(self, val_a, val_b, val_c, val_d):
        cond_a = val_a > self.threshold_low
        cond_b = val_b < self.threshold_high
        cond_c = val_c == self.equality_target
        cond_d = val_d is not None

        combined = cond_a and cond_b
        combined = combined or cond_c
        combined = combined and cond_d

        return bool(combined)

    def get_thresholds(self):
        return (self.threshold_low, self.threshold_high)

if __name__ == '__main__':
    evaluator = ConditionEvaluator(0, 10, 5)
    result_one = evaluator.evaluate(5, 8, 10, 10)
    result_two = evaluator.evaluate(10, 5, 5, "value")
    print(result_one)
    print(result_two)
    print(evaluator.get_thresholds())