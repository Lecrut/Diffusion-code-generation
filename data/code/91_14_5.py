def flip_bool_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_values = {True: False, False: True}
    for original, expected in sample_values.items():
        result = flip_bool_value(original)
        print(f"Original: {original}, Expected: {expected}, Result: {result}")