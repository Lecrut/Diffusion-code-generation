class BooleanChecker:
    def are_both_false(self, val1, val2):
        if val1 is not False:
            return False
        if val2 is not False:
            return False
        return True

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)