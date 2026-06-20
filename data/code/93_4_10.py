class BooleanChecker:
    @staticmethod
    def is_false(val):
        return not bool(val)

    @classmethod
    def determine_both_false(cls, val1, val2):
        return cls.is_false(val1) and cls.is_false(val2)

if __name__ == '__main__':
    print(BooleanChecker.determine_both_false(0, 0))
    print(BooleanChecker.determine_both_false('hello', ''))
    print(BooleanChecker.determine_both_false(None, None))
    print(BooleanChecker.determine_both_false(True, False))