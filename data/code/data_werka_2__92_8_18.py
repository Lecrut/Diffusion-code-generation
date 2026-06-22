BIT_MASK = 1

def get_bitwise_negation(flag):
    inverted_value = ~flag
    masked_result = inverted_value & BIT_MASK
    is_opposite = bool(masked_result)
    return is_opposite

if __name__ == '__main__':
    sample_true = True
    sample_false = False
    result_from_true = get_bitwise_negation(sample_true)
    result_from_false = get_bitwise_negation(sample_false)
    print(result_from_true)
    print(result_from_false)