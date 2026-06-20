class ConditionChecker:
    @staticmethod
    def check_condition(*args):
        return any(args)

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(True, False, False))
    print(checker.check_condition(False, False, True))
    print(checker.check_condition(False, False, False))