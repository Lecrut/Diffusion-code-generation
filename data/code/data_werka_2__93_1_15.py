def are_both_false(a, b):
    def _validate_bool(val, name):
        if not isinstance(val, bool):
            raise ValueError(f"{name} must be a boolean")
        return val

    is_first_false = _validate_bool(a, "a") is False
    is_second_false = _validate_bool(b, "b") is False
    return is_first_false and is_second_false

if __name__ == '__main__':
    result1 = are_both_false(False, False)
    print(result1)
    result2 = are_both_false(True, False)
    print(result2)
    result3 = are_both_false(False, True)
    print(result3)
    result4 = are_both_false(True, True)
    print(result4)