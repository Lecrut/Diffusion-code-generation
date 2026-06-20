class ConditionChecker:
    @staticmethod
    def check_conjunction(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(ConditionChecker.check_conjunction(True, True))
    print(ConditionChecker.check_conjunction(False, True))
    print(ConditionChecker.check_conjunction(True, False))
    print(ConditionChecker.check_conjunction(False, False))