class ConditionEvaluator:
    def __init__(self, threshold_a, threshold_b, reference_c):
        self.threshold_a = threshold_a
        self.threshold_b = threshold_b
        self.reference_c = reference_c

    def evaluate(self, val_a, val_b, val_c, val_d):
        cond_a = val_a > self.threshold_a
        cond_b = val_b < self.threshold_b
        cond_c = val_c == self.reference_c
        cond_d = val_d is not None
        
        if cond_a and cond_b:
            return cond_c and cond_d
        return cond_c or cond_d

if __name__ == '__main__':
    evaluator = ConditionEvaluator(0, 10, 5)
    result1 = evaluator.evaluate(5, 8, 5, "value")
    print(result1)
    result2 = evaluator.evaluate(-1, 15, 5, None)
    print(result2)