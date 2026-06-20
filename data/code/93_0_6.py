def is_false(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value

def check_both_false(a, b):
    return is_false(a) and is_false(b)

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)