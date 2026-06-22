class BooleanChecker:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def _to_bool(self, val):
        if isinstance(val, bool):
            return val
        if val is None:
            return False
        if isinstance(val, (int, float)):
            return val != 0
        if isinstance(val, (list, tuple, dict, set, str)):
            return len(val) > 0
        return bool(val)

    def determine_both_false(self):
        bool1 = self._to_bool(self.val1)
        bool2 = self._to_bool(self.val2)
        return not bool1 and not bool2

if __name__ == '__main__':
    checker = BooleanChecker(0, 0)
    print(checker.determine_both_false())
    checker2 = BooleanChecker(1, 0)
    print(checker2.determine_both_false())
    checker3 = BooleanChecker(None, None)
    print(checker3.determine_both_false())
    checker4 = BooleanChecker([], {})
    print(checker4.determine_both_false())
    checker5 = BooleanChecker([1], {1: 1})
    print(checker5.determine_both_false())