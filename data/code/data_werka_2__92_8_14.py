def invert_boolean_bitwise(flag):
    if not isinstance(flag, bool):
        raise ValueError("Input must be a boolean")
    inverted_int = ~int(flag)
    masked = inverted_int & 1
    return bool(masked)

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    result_true = invert_boolean_bitwise(sample_true)
    result_false = invert_boolean_bitwise(sample_false)
    print(result_true)
    print(result_false)