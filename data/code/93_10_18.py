class BooleanChecker:
    _VALID_TYPES = (bool,)

    @staticmethod
    def _validate_boolean(value):
        if not isinstance(value, BooleanChecker._VALID_TYPES):
            raise ValueError(f"Expected boolean, got {type(value).__name__}")
        return value

    def are_both_false(self, val1, val2):
        v1 = self._validate_boolean(val1)
        v2 = self._validate_boolean(val2)
        return v1 is False and v2 is False

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)