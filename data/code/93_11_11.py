class BooleanChecker:
    def validate_input(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean value.")

    def are_both_false(self, a, b):
        self.validate_input(a)
        self.validate_input(b)
        return not a and not b

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.are_both_false(False, False))
    print(checker.are_both_false(True, False))
    print(checker.are_both_false(False, True))
    print(checker.are_both_false(True, True))