class ConditionChecker:

    @staticmethod
    def check_conjunction(a: bool, b: bool) -> bool:
        return a and b
if __name__ == '__main__':
    result1 = ConditionChecker.check_conjunction(True, True)
    result2 = ConditionChecker.check_conjunction(False, True)
    result3 = ConditionChecker.check_conjunction(True, False)
    result4 = ConditionChecker.check_conjunction(False, False)
    print(result1)
    print(result2)
    print(result3)
    print(result4)