def validate_and_check_false(first: bool, second: bool) -> bool:
    if not isinstance(first, bool) or not isinstance(second, bool):
        raise ValueError("Inputs must be boolean type")
    return not first and not second

if __name__ == '__main__':
    val_a = False
    val_b = False
    result = validate_and_check_false(val_a, val_b)
    print(result)