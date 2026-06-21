BOOLEAN_MAP = {
    True: False,
    False: True
}

def flip_bool_value(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return BOOLEAN_MAP[value]

if __name__ == '__main__':
    input_val = True
    output_val = flip_bool_value(input_val)
    print(output_val)