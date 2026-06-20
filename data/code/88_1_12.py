class ConditionChecker:
    @staticmethod
    def both_conditions_true(a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    condition_a = True
    condition_b = False
    print(f"both_conditions_true({condition_a}, {condition_b}): {ConditionChecker.both_conditions_true(condition_a, condition_b)}")