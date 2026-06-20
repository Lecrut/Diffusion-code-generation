def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return not a and not b

if __name__ == '__main__':
    sample_values = (False, False)
    result = check_both_false(*sample_values)
    print(result)