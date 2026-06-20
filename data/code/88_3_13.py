class ConditionChecker:
    @staticmethod
    def check_conditions_met(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(ConditionChecker.check_conditions_met(True, True))
    print(ConditionChecker.check_conditions_met(False, True))
    print(ConditionChecker.check_conditions_met(True, False))
    print(ConditionChecker.check_conditions_met(False, False))