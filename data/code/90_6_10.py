class ConditionChecker:
    @staticmethod
    def check_conditions(*conditions):
        return any(conditions)

if __name__ == '__main__':
    condition1 = 5 > 3
    condition2 = 7 < 4
    print("Conditions met:", ConditionChecker.check_conditions(condition1, condition2))