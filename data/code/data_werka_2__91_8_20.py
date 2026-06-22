def validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean type")
    return value

def negate_boolean(value):
    validate_boolean(value)
    return value is False

def process_boolean(value):
    original = value
    negated = negate_boolean(value)
    return original, negated

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    orig1, neg1 = process_boolean(sample_true)
    print(f"Original: {orig1}, Negated: {neg1}")
    orig2, neg2 = process_boolean(sample_false)
    print(f"Original: {orig2}, Negated: {neg2}")