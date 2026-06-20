def flip_bool_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    test_values = [True, False]
    for val in test_values:
        print(f"Flipping {val}: {flip_bool_value(val)}")