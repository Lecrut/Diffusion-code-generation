class BoolChecker:

    @staticmethod
    def both_false(a, b):
        return not (a or b)
if __name__ == '__main__':
    check = BoolChecker()
    print(check.both_false(False, False))
    print(check.both_false(True, False))
    print(check.both_false(False, True))
    print(check.both_false(True, True))