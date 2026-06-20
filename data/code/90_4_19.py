class ConditionEvaluator:
    def evaluate_or_conditions(self, conditions):
        return [any(condition) for condition in conditions]

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    sample_conditions1 = [(True, False), (False, False), (True, True)]
    print(evaluator.evaluate_or_conditions(sample_conditions1))
    sample_conditions2 = [(False, False), (False, False), (False, False)]
    print(evaluator.evaluate_or_conditions(sample_conditions2))
    sample_conditions3 = [(True, True), (True, True), (True, True)]
    print(evaluator.evaluate_or_conditions(sample_conditions3))