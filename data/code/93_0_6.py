def is_false(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value is False

def verify_both_false(first_input, second_input):
    is_first_false = is_false(first_input)
    is_second_false = is_false(second_input)
    return is_first_false and is_second_false

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = verify_both_false(val_a, val_b)
    print(outcome)