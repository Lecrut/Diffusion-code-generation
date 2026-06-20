def validate_input(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return True

def flip_bool_value(value: bool) -> bool:
    validate_input(value)
    return not value

if __name__ == '__main__':
    sample_true = True
    print(f"Flipping {sample_true}: {flip_bool_value(sample_true)}")
    sample_false = False
    print(f"Flipping {sample_false}: {flip_bool_value(sample_false)}")