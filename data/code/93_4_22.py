class BooleanChecker:
    FALSE_VALUE = 0
    TRUE_VALUE = 1

    @staticmethod
    def _coerce_to_bool(value):
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != BooleanChecker.FALSE_VALUE
        if isinstance(value, str):
            return len(value) > 0
        if isinstance(value, (list, tuple, dict, set)):
            return len(value) > 0
        if value is None:
            return False
        return bool(value)

    @staticmethod
    def determine_both_false(val1, val2):
        is_val1_false = not BooleanChecker._coerce_to_bool(val1)
        is_val2_false = not BooleanChecker._coerce_to_bool(val2)
        return is_val1_false and is_val2_false

if __name__ == '__main__':
    result = BooleanChecker.determine_both_false(0, 0)
    print(result)
    result = BooleanChecker.determine_both_false(False, False)
    print(result)
    result = BooleanChecker.determine_both_false(None, None)
    print(result)
    result = BooleanChecker.determine_both_false([], {})
    print(result)
    result = BooleanChecker.determine_both_false([1], {1: 1})
    print(result)
    result = BooleanChecker.determine_both_false(1, 0)
    print(result)
    result = BooleanChecker.determine_both_false("", "")
    print(result)
    result = BooleanChecker.determine_both_false("false", "false")
    print(result)