class ConditionChecker:
    @staticmethod
    def check_condition(*args):
        return any(args)

if __name__ == '__main__':
    print(ConditionChecker.check_condition(True, False, False))
    print(ConditionChecker.check_condition(False, False, True))
    print(ConditionChecker.check_condition(False, False, False))