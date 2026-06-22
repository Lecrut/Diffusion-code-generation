class BooleanChecker:
    _VALID_TYPES = (bool,)

    def _validate_boolean(self, val):
        if not isinstance(val, self._VALID_TYPES):
            raise ValueError("Input must be a boolean")
        return val

    def are_both_false(self, val1, val2):
        validated_v1 = self._validate_boolean(val1)
        validated_v2 = self._validate_boolean(val2)
        return validated_v1 is False and validated_v2 is False

if __name__ == '__main__':
    checker = BooleanChecker()
    result = checker.are_both_false(False, False)
    print(result)