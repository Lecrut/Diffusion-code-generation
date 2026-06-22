def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Arguments must be boolean")
    return not (a or b)

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)