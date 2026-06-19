class ConditionChecker:
    def check_condition(self, a, b):
        return a == b

if __name__ == '__main__':
    sample1_a = 10
    sample1_b = 10
    checker = ConditionChecker()
    result1 = checker.check_condition(sample1_a, sample1_b)
    print(result1)

    sample2_a = 25
    sample2_b = 30
    result2 = checker.check_condition(sample2_a, sample2_b)
    print(result2)

    sample3_a = -7
    sample3_b = -7
    result3 = checker.check_condition(sample3_a, sample3_b)
    print(result3)

    sample4_a = 0
    sample4_b = 1
    result4 = checker.check_condition(sample4_a, sample4_b)
    print(result4)