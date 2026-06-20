class ConditionEvaluator:
    def evaluate_conditions(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(f"evaluate_conditions(True, True): {evaluator.evaluate_conditions(True, True)}")
    print(f"evaluate_conditions(True, False): {evaluator.evaluate_conditions(True, False)}")
    print(f"evaluate_conditions(False, True): {evaluator.evaluate_conditions(False, True)}")
    print(f"evaluate_conditions(False, False): {evaluator.evaluate_conditions(False, False)}")