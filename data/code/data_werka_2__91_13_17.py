def negate_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return bool(value ^ 1)

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        result = negate_boolean(val)
        print(result)