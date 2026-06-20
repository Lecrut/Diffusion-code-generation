class ConditionChecker:
    @staticmethod
    def both_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    print(f"both_true(True, True): {ConditionChecker.both_true(True, True)}")
    print(f"both_true(True, False): {ConditionChecker.both_true(True, False)}")
    print(f"both_true(False, True): {ConditionChecker.both_true(False, True)}")
    print(f"both_true(False, False): {ConditionChecker.both_true(False, False)}")