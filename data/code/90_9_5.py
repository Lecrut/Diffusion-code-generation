class ConditionEvaluator:
    @staticmethod
    def check_condition(*args):
        return any(args)

if __name__ == '__main__':
    print(ConditionEvaluator.check_condition(True, False, False))
    print(ConditionEvaluator.check_condition(False, False, True))
    print(ConditionEvaluator.check_condition(False, False, False))