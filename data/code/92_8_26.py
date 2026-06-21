def compute_logical_inversion(boolean_flag):
    bitwise_inverted = ~boolean_flag
    mask = 1
    numeric_opposite = bitwise_inverted & mask
    return bool(numeric_opposite)

if __name__ == '__main__':
    sample_positive = True
    sample_negative = False
    result_for_positive = compute_logical_inversion(sample_positive)
    result_for_negative = compute_logical_inversion(sample_negative)
    print(result_for_positive)
    print(result_for_negative)