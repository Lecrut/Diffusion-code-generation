class ConditionEvaluator:
    @staticmethod
    def are_conditions_met(condition_a, condition_b):
        return condition_a and condition_b

if __name__ == '__main__':
    result = ConditionEvaluator.are_conditions_met(True, False)
    print(result)