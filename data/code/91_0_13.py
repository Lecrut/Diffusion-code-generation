def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    sample_value = True
    negated_sample = negate_boolean(sample_value)
    print(f"Original value: {sample_value}")
    print(f"Negated value: {negated_sample}")