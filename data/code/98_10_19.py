class ConditionChecker:
    def check_all(self, *conditions):
        return all(conditions)

if __name__ == '__main__':
    checker = ConditionChecker()
    condition_a = True
    condition_b = False
    condition_c = True
    result = checker.check_all(condition_a, condition_b, condition_c)
    print(f"Condition A: {condition_a}")
    print(f"Condition B: {condition_b}")
    print(f"Condition C: {condition_c}")
    print(f"All conditions met: {result}")

    condition_d = True
    condition_e = True
    result = checker.check_all(condition_d, condition_e)
    print(f"\nCondition D: {condition_d}")
    print(f"Condition E: {condition_e}")
    print(f"All conditions met: {result}")