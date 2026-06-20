class ConditionChecker:

    def check_and(self, a: bool, b: bool) -> bool:
        return a and b
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_and(True, True))
    print(checker.check_and(False, True))
    print(checker.check_and(True, False))
    print(checker.check_and(False, False))