class BooleanChecker:
    def check_both_false(self, a: bool, b: bool) -> bool:
        return not (a or b)

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.check_both_false(False, False)
    print(result)