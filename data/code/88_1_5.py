class ConditionEvaluator:
    def evaluate_conditions(self, condition_a: bool, condition_b: bool) -> bool:
        return condition_a and condition_b

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(f"evaluate_conditions(True, True): {evaluator.evaluate_conditions(True, True)}")
    print(f"evaluate_conditions(True, False): {evaluator.evaluate_conditions(True, False)}")
    print(f"evaluate_conditions(False, True): {evaluator.evaluate_conditions(False, True)}")
    print(f"evaluate_conditions(False, False): {evaluator.evaluate_conditions(False, False)}")