def flip_bool_value(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

if __name__ == '__main__':
    test_value_true = True
    result_true = flip_bool_value(test_value_true)
    print(f"Flipping {test_value_true}: {result_true}")
    
    test_value_false = False
    result_false = flip_bool_value(test_value_false)
    print(f"Flipping {test_value_false}: {result_false}")