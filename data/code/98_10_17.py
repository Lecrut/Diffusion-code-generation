class ConditionChecker:
    @staticmethod
    def check_all(*conditions):
        return all(conditions)

if __name__ == '__main__':
    condition_a = True
    condition_b = False
    condition_c = True
    result = ConditionChecker.check_all(condition_a, condition_b, condition_c)
    print(f"Condition A: {condition_a}")
    print(f"Condition B: {condition_b}")
    print(f"Condition C: {condition_c}")
    print(f"Result of all conditions being met: {result}")