def convert_to_boolean(raw_input):
    if isinstance(raw_input, bool):
        return raw_input
    if isinstance(raw_input, str):
        lower_val = raw_input.lower()
        if lower_val == 'true':
            return True
        if lower_val == 'false':
            return False
    if isinstance(raw_input, (int, float)):
        if raw_input == 1 or raw_input == 0:
            return bool(raw_input)
    raise ValueError(f"Cannot convert {type(raw_input)} to boolean")

def negate_boolean(input_value):
    is_valid_bool = convert_to_boolean(input_value)
    return not is_valid_bool

if __name__ == '__main__':
    test_inputs = [True, False, 'True', 'False', 1, 0]
    for item in test_inputs:
        negated = negate_boolean(item)
        print(negated)