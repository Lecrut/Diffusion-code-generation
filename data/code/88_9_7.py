class BooleanChecker:
    def is_both_true(self, a: bool, b: bool) -> bool:
        return a and b

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.is_both_true(True, True)
    print(result)