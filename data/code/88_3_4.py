class ConditionChecker:
    def check_conditions_met(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_conditions_met(True, True))
    print(checker.check_conditions_met(False, True))
    print(checker.check_conditions_met(True, False))
    print(checker.check_conditions_met(False, False))