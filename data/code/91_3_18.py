def validate_boolean(value: bool) -> None:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")

def opposite_boolean(value: bool) -> bool:
    validate_boolean(value)
    return not value

if __name__ == '__main__':
    test_values = [True, False]
    for val in test_values:
        print(opposite_boolean(val))