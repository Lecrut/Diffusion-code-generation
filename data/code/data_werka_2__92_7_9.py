def invert_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return value ^ True

if __name__ == '__main__':
    sample_value = True
    result = invert_boolean(sample_value)
    print(result)
    sample_value = False
    result = invert_boolean(sample_value)
    print(result)