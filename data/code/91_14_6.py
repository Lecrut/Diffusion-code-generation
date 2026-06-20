def flip_bool_value(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

if __name__ == '__main__':
    test_values = [True, False]
    for val in test_values:
        try:
            result = flip_bool_value(val)
            print(f"Inverting {val}: {result}")
        except ValueError as e:
            print(e)