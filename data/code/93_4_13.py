class BoolChecker:
    def determine_both_false(self, val1, val2):
        return not bool(val1) and not bool(val2)

if __name__ == '__main__':
    checker = BoolChecker()
    print(checker.determine_both_false(0, 0))
    print(checker.determine_both_false('hello', ''))
    print(checker.determine_both_false(None, None))
    print(checker.determine_both_false(True, False))