class ConditionEvaluator:
    @staticmethod
    def check_combined_conditions(bool1: bool, bool2: bool) -> bool:
        return bool1 or bool2

if __name__ == '__main__':
    result1 = ConditionEvaluator.check_combined_conditions(True, False)
    print(result1)
    result2 = ConditionEvaluator.check_combined_conditions(False, True)
    print(result2)
    result3 = ConditionEvaluator.check_combined_conditions(True, True)
    print(result3)
    result4 = ConditionEvaluator.check_combined_conditions(False, False)
    print(result4)