def validate_bool(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    return value

def check_both_false(a, b):
    is_a_false = validate_bool(a) is False
    is_b_false = validate_bool(b) is False
    return is_a_false and is_b_false

if __name__ == '__main__':
    val_a = False
    val_b = False
    print(check_both_false(val_a, val_b))
    val_a = True
    val_b = False
    print(check_both_false(val_a, val_b))