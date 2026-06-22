class BooleanChecker:
    def are_both_false(self, val1, val2):
        return not val1 and not val2

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)