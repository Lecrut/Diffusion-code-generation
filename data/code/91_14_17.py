def flip_bool_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_values = {True: 'on', False: 'off'}
    for input_val, description in sample_values.items():
        inverted_val = flip_bool_value(input_val)
        print(f"Inverting {description} ({input_val}): {inverted_val}")