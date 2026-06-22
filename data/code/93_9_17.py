def _validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Argument must be a boolean")
    return value

def check_both_false(a, b):
    is_a_false = _validate_boolean(a) is False
    is_b_false = _validate_boolean(b) is False
    return is_a_false and is_b_false

if __name__ == '__main__':
    val1 = False
    val2 = False
    output = check_both_false(val1, val2)
    print(output)