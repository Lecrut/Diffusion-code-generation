def flip_bool_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    test_values = {True: "True", False: "False"}
    for key, val in test_values.items():
        result = flip_bool_value(key)
        print(f"Flipping {val}: {result}")