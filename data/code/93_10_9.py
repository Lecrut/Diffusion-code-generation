def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("First input must be a boolean value.")
    if not isinstance(b, bool):
        raise ValueError("Second input must be a boolean value.")
    return not a and not b

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)