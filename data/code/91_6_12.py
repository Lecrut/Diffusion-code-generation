def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def negate_boolean(value):
    validate_boolean(value)
    return not value

if __name__ == '__main__':
    sample_value = True
    negated_value = negate_boolean(sample_value)
    print(negated_value)