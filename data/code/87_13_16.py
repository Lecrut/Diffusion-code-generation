class ConditionChecker:
    @staticmethod
    def check_conditions(a: bool, b: bool) -> bool:
        return (a and not b) or (not a and b)

if __name__ == '__main__':
    print(ConditionChecker.check_conditions(True, False))
    print(ConditionChecker.check_conditions(False, True))
    print(ConditionChecker.check_conditions(True, True))
    print(ConditionChecker.check_conditions(False, False))