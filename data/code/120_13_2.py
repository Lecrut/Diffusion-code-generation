class ValueChecker:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    value1_a = 10
    value2_a = 10
    result_a = checker.check_equality(value1_a, value2_a)
    print(f"Checking {value1_a} and {value2_a}: {result_a}")
    value1_b = 5
    value2_b = 8
    result_b = checker.check_equality(value1_b, value2_b)
    print(f"Checking {value1_b} and {value2_b}: {result_b}")
    value1_c = "hello"
    value2_c = "hello"
    result_c = checker.check_equality(value1_c, value2_c)
    print(f"Checking '{value1_c}' and '{value2_c}': {result_c}")
    value1_d = 3.14
    value2_d = 3.1400000000000001
    result_d = checker.check_equality(value1_d, value2_d)
    print(f"Checking {value1_d} and {value2_d}: {result_d}")