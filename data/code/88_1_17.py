class ConditionChecker:
    def both_conditions_met(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    checker = ConditionChecker()
    print(f"both_conditions_met(True, True): {checker.both_conditions_met(True, True)}")
    print(f"both_conditions_met(True, False): {checker.both_conditions_met(True, False)}")
    print(f"both_conditions_met(False, True): {checker.both_conditions_met(False, True)}")
    print(f"both_conditions_met(False, False): {checker.both_conditions_met(False, False)}")