class BooleanChecker:
    def are_both_false(self, a, b):
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)