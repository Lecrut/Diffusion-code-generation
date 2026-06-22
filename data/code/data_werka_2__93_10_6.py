class BooleanChecker:
    FALSE_VALUE = False

    def are_both_false(self, val1, val2):
        return val1 == self.FALSE_VALUE and val2 == self.FALSE_VALUE

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)