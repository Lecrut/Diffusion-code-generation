def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return not a and not b

if __name__ == '__main__':
    result1 = check_both_false(False, False)
    print(f"False, False -> {result1}")
    result2 = check_both_false(True, False)
    print(f"True, False -> {result2}")
    result3 = check_both_false(True, True)
    print(f"True, True -> {result3}")
    result4 = check_both_false(False, True)
    print(f"False, True -> {result4}")