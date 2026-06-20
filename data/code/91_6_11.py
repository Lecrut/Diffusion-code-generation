def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")
    return not value

if __name__ == '__main__':
    sample_value = True
    try:
        negated_value = negate_boolean(sample_value)
        print(negated_value)
    except ValueError as e:
        print(e)