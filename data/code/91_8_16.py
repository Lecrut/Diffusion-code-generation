def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    sample_value_true = True
    print(f"Original: {sample_value_true}, Negated: {negate_boolean(sample_value_true)}")
    sample_value_false = False
    print(f"Original: {sample_value_false}, Negated: {negate_boolean(sample_value_false)}")