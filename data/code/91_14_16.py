def flip_bool_value(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    mapping = {True: False, False: True}
    return mapping[value]

if __name__ == '__main__':
    result_a = flip_bool_value(True)
    result_b = flip_bool_value(False)
    print(result_a)
    print(result_b)