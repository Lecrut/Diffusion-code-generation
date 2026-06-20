def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def flip_bool_value(value: bool) -> bool:
    validate_input(value)
    return not value

if __name__ == '__main__':
    test_values = [True, False]
    for val in test_values:
        print(f"Flipping {val}: {flip_bool_value(val)}")