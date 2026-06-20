class BoolChecker:
    @staticmethod
    def is_false(value):
        return not bool(value)

    @classmethod
    def determine_both_false(cls, val1, val2):
        return cls.is_false(val1) and cls.is_false(val2)

if __name__ == '__main__':
    print(BoolChecker.determine_both_false(0, 0))
    print(BoolChecker.determine_both_false('hello', ''))
    print(BoolChecker.determine_both_false(None, None))
    print(BoolChecker.determine_both_false(True, False))