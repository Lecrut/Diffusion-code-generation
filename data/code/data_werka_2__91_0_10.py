def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    is_true = value is True
    is_false = value is False
    if is_true:
        return is_false
    return is_true

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    negated_true = negate_boolean(sample_true)
    negated_false = negate_boolean(sample_false)
    print(negated_true)
    print(negated_false)