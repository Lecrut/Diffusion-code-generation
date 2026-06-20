class BooleanChecker:
    def both_false(self, a: bool, b: bool) -> bool:
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    result1 = checker.both_false(False, False)
    print(result1)
    result2 = checker.both_false(True, False)
    print(result2)
    result3 = checker.both_false(False, True)
    print(result3)
    result4 = checker.both_false(True, True)
    print(result4)