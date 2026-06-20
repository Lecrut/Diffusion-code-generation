def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return not a and not b

if __name__ == '__main__':
    try:
        result = check_both_false(False, False)
        print(result)
    except ValueError as e:
        print(e)