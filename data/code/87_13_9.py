class ConditionChecker:
    def check_conditions(self, a: bool, b: bool) -> bool:
        return (a and not b) or (not a and b)

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_conditions(True, False))
    print(checker.check_conditions(False, True))
    print(checker.check_conditions(True, True))
    print(checker.check_conditions(False, False))