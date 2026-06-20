class BooleanChecker:
    def are_both_false(self, a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Both inputs must be boolean values.")
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(False, False))
    print(checker.are_both_false(True, False))
    print(checker.are_both_false(False, True))
    print(checker.are_both_false(True, True))