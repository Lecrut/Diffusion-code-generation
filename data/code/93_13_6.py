def _validate_boolean(value: object) -> None:
    if not isinstance(value, bool):
        raise ValueError("Argument must be a boolean")

def check_both_false(a: bool, b: bool) -> bool:
    _validate_boolean(a)
    _validate_boolean(b)
    return (a ^ b) and not a

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)
    result2 = check_both_false(True, False)
    print(result2)
    result3 = check_both_false(False, True)
    print(result3)
    result4 = check_both_false(True, True)
    print(result4)