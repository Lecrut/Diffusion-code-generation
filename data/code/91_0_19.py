def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    sample_values = [True, False, "not a boolean"]
    for val in sample_values:
        try:
            result = negate_boolean(val)
            print(f"Original value: {val}, Negated value: {result}")
        except ValueError as e:
            print(e)