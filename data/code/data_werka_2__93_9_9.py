def _validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value

def check_both_false(first, second):
    is_first_bool = _validate_boolean(first)
    is_second_bool = _validate_boolean(second)
    return is_first_bool is False and is_second_bool is False

if __name__ == '__main__':
    val_a = False
    val_b = False
    output = check_both_false(val_a, val_b)
    print(output)