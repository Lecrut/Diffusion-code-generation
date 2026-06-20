class ConditionEvaluator:
    def __init__(self, condition_a, condition_b):
        self.condition_a = condition_a
        self.condition_b = condition_b
    
    def evaluate_conditions(self):
        return self.condition_a and self.condition_b

if __name__ == '__main__':
    evaluator = ConditionEvaluator(True, False)
    result = evaluator.evaluate_conditions()
    print(result)