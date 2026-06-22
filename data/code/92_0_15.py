def negate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    return not value

if __name__ == '__main__':
    sample_true = True
    result_true = negate_boolean(sample_true)
    print(result_true)

    sample_false = False
    result_false = negate_boolean(sample_false)
    print(result_false)