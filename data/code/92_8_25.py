BITWISE_MASK = 1

def invert_boolean_bitwise(flag_value):
    inverted_integer = ~flag_value
    masked_value = inverted_integer & BITWISE_MASK
    return bool(masked_value)

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    result_true = invert_boolean_bitwise(sample_true)
    result_false = invert_boolean_bitwise(sample_false)
    print(result_true)
    print(result_false)