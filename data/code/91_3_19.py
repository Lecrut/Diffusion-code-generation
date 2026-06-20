def opposite_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(opposite_boolean(val))