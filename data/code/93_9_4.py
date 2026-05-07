class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not a and not b
if __name__ == '__main__':
    checker = BooleanChecker()
    a1 = False
    b1 = False
    result1 = checker.check_both_false(a1, b1)
    print(f"Checking ({a1}, {b1}): {result1}")
    a2 = True
    b2 = False
    result2 = checker.check_both_false(a2, b2)
    print(f"Checking ({a2}, {b2}): {result2}")
    a3 = False
    b3 = True
    result3 = checker.check_both_false(a3, b3)
    print(f"Checking ({a3}, {b3}): {result3}")
    a4 = True
    b4 = True
    result4 = checker.check_both_false(a4, b4)
    print(f"Checking ({a4}, {b4}): {result4}")