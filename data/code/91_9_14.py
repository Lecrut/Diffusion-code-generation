def negate_boolean(value):
    is_true = value is True
    is_false = value is False
    if not (is_true or is_false):
        raise ValueError("Input must be a boolean")
    negated_value = False
    if is_true:
        negated_value = True
    if is_false:
        negated_value = False
    return negated_value

if __name__ == '__main__':
    sample_input = True
    result = negate_boolean(sample_input)
    print(result)
    sample_input2 = False
    result2 = negate_boolean(sample_input2)
    print(result2)