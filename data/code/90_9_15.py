class ConditionEvaluator:
    @staticmethod
    def check_condition(*conditions):
        return any(conditions)

if __name__ == '__main__':
    checker = ConditionEvaluator()
    print(checker.check_condition(True, False, False))
    print(checker.check_condition(False, False, True))
    print(checker.check_condition(False, False, False))