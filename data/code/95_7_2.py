class AttributeChecker:
    def combine_checks(self, a, b, c):
        check_a_positive = a > 0
        check_b_even = b % 2 == 0
        check_c_divisible_by_a = a != 0 and c % a == 0
        result = check_a_positive and check_b_even and check_c_divisible_by_a
        return result
if __name__ == '__main__':
    checker = AttributeChecker()
    a1, b1, c1 = 2, 4, 6
    result1 = checker.combine_checks(a1, b1, c1)
    print(f"a={a1}, b={b1}, c={c1}: {result1}")
    a2, b2, c2 = 3, 4, 6
    result2 = checker.combine_checks(a2, b2, c2)
    print(f"a={a2}, b={b2}, c={c2}: {result2}")
    a3, b3, c3 = 1, 3, 5
    result3 = checker.combine_checks(a3, b3, c3)
    print(f"a={a3}, b={b3}, c={c3}: {result3}")
    a4, b4, c4 = 0, 2, 4
    result4 = checker.combine_checks(a4, b4, c4)
    print(f"a={a4}, b={b4}, c={c4}: {result4}")
    a5, b5, c5 = 5, 10, 15
    result5 = checker.combine_checks(a5, b5, c5)
    print(f"a={a5}, b={b5}, c={c5}: {result5}")