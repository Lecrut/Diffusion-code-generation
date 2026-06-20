class ConditionChecker:
    def both_conditions_true(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    checker = ConditionChecker()
    print(f"both_conditions_true(True, True): {checker.both_conditions_true(True, True)}")
    print(f"both_conditions_true(True, False): {checker.both_conditions_true(True, False)}")
    print(f"both_conditions_true(False, True): {checker.both_conditions_true(False, True)}")
    print(f"both_conditions_true(False, False): {checker.both_conditions_true(False, False)}")