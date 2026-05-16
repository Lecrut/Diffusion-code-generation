class AttributeChecker:
    def combine_checks(self, a, b, c):
        check_a_positive = a > 0
        check_b_even = b % 2 == 0
        check_c_divisible_by_a = a != 0 and c % a == 0
        result = check_a_positive and check_b_even and check_c_divisible_by_a
        return result
if __name__ == '__main__':
    checker = AttributeChecker()
    a_val = 5
    b_val = 8
    c_val = 20
    result = checker.combine_checks(a_val, b_val, c_val)
    print(result)
    a_val = -5
    b_val = 8
    c_val = 20
    result = checker.combine_checks(a_val, b_val, c_val)
    print(result)
    a_val = 10
    b_val = 7
    c_val = 30
    result = checker.combine_checks(a_val, b_val, c_val)
    print(result)