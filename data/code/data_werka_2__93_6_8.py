def check_both_false(a, b):
    if not isinstance(a, (bool, int, float, str, list, tuple, dict, set, type(None))):
        raise ValueError(f"Unsupported type for a: {type(a)}")
    if not isinstance(b, (bool, int, float, str, list, tuple, dict, set, type(None))):
        raise ValueError(f"Unsupported type for b: {type(b)}")
    return (not a) and (not b)

if __name__ == '__main__':
    a = 0
    b = False
    result = check_both_false(a, b)
    print(result)