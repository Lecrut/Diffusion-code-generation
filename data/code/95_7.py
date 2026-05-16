class AttributeChecker:
    def combine_checks(self, a, b, c):
        check_a = a > 0
        check_b = b % 2 == 0
        check_c = c % a == 0
        result = check_a and check_b and check_c
        return result
if __name__ == '__main__':
    checker = AttributeChecker()
    print(f"Test 1 (a=2, b=4, c=6): {checker.combine_checks(2, 4, 6)}")
    print(f"Test 2 (a=3, b=5, c=7): {checker.combine_checks(3, 5, 7)}")
    print(f"Test 3 (a=-1, b=2, c=4): {checker.combine_checks(-1, 2, 4)}")
    print(f"Test 4 (a=2, b=3, c=5): {checker.combine_checks(2, 3, 5)}")
    print(f"Test 5 (a=5, b=4, c=10): {checker.combine_checks(5, 4, 10)}")
    print(f"Test 6 (a=1, b=2, c=5): {checker.combine_checks(1, 2, 5)}")
    print(f"Test 7 (a=1, b=3, c=5): {checker.combine_checks(1, 3, 5)}")