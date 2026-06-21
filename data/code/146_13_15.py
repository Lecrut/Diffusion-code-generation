class ConditionEvaluator:
    CONDITION_A = "Condition A met"
    CONDITION_B_HIGH = "Condition B met (High)"
    CONDITION_B_LOW = "Condition B met (Low)"
    CONDITION_C = "Condition C met"
    DEFAULT_CONDITION = "Default Condition"

    @staticmethod
    def evaluate_conditions(value1, value2, value3=None):
        if value1 > 10 and value2 < 5:
            return ConditionEvaluator.CONDITION_A
        elif value1 <= 10 and value2 >= 5:
            if value3 is not None and value3 > 20:
                return ConditionEvaluator.CONDITION_B_HIGH
            else:
                return ConditionEvaluator.CONDITION_B_LOW
        elif value1 > 5 and value2 > 15:
            return ConditionEvaluator.CONDITION_C
        else:
            return ConditionEvaluator.DEFAULT_CONDITION

if __name__ == '__main__':
    evaluator = ConditionEvaluator()
    print(evaluator.evaluate_conditions(12, 3))
    print(evaluator.evaluate_conditions(8, 7))
    print(evaluator.evaluate_conditions(6, 15))
    print(evaluator.evaluate_conditions(10, 5))
    print(evaluator.evaluate_conditions(1, 1))