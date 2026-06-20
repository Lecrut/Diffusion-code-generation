def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

if __name__ == '__main__':
    sample_value = True
    try:
        result = negate_boolean(sample_value)
        print(result)
    except ValueError as e:
        print(e)