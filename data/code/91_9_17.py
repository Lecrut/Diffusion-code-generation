def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(f"Original value: {val}")
        print(f"Negated value: {negate_boolean(val)}")