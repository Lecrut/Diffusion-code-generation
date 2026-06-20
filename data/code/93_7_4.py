class CheckBools:
    def are_both_false(self, a, b):
        return not a and not b

if __name__ == '__main__':
    check = CheckBools()
    print(check.are_both_false(False, False))
    print(check.are_both_false(True, False))
    print(check.are_both_false(False, True))
    print(check.are_both_false(True, True))