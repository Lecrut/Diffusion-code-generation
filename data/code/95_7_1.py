class AttributeChecker:
    def check_attributes(self, a, b, c):
        is_a_positive = a > 0
        is_b_even = b % 2 == 0
        is_c_divisible_by_a = a != 0 and c % a == 0
        result = is_a_positive and is_b_even and is_c_divisible_by_a
        return result
if __name__ == '__main__':
    checker = AttributeChecker()
    a_val = 10
    b_val = 12
    c_val = 30
    result = checker.check_attributes(a_val, b_val, c_val)
    print(result)