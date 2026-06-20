class ConditionEvaluator:
    @staticmethod
    def evaluate_conditions(condition_a: bool, condition_b: bool) -> bool:
        return condition_a and condition_b

if __name__ == '__main__':
    result = ConditionEvaluator.evaluate_conditions(True, False)
    print(result)