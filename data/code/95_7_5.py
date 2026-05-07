class AttributeChecker:
    def combine_checks(self, a, b, c):
        check_a = a > 0
        check_b = b % 2 == 0
        check_c = c % a == 0
        return check_a and check_b and check_c
if __name__ == '__main__':
    checker = AttributeChecker()
    a1, b1, c1 = 2, 4, 6
    result1 = checker.combine_checks(a1, b1, c1)
    print(f"a={a1}, b={b1}, c={c1}: {result1}")
    a2, b2, c2 = -2, 4, 6
    result2 = checker.combine_checks(a2, b2, c2)
    print(f"a={a2}, b={b2}, c={c2}: {result2}")
    a3, b3, c3 = 2, 5, 6
    result3 = checker.combine_checks(a3, b3, c3)
    print(f"a={a3}, b={b3}, c={c3}: {result3}")
    a4, b4, c4 = 3, 4, 7
    result4 = checker.combine_checks(a4, b4, c4)
    print(f"a={a4}, b={b4}, c={c4}: {result4}")
    a5, b5, c5 = -1, 5, 10
    result5 = checker.combine_checks(a5, b5, c5)
    print(f"a={a5}, b={b5}, c={c5}: {result5}")