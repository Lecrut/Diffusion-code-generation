def both_false(a: bool, b: bool) -> bool:
    def validate_bool(val):
        if not isinstance(val, bool):
            raise ValueError("Input must be a boolean")
        return val

    valid_a = validate_bool(a)
    valid_b = validate_bool(b)

    return valid_a is False and valid_b is False

if __name__ == '__main__':
    result1 = both_false(False, False)
    print(result1)
    result2 = both_false(True, False)
    print(result2)
    result3 = both_false(False, True)
    print(result3)
    result4 = both_false(True, True)
    print(result4)