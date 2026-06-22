def invert_boolean_bitwise(flag):
    bit_representation = int(flag)
    flipped_bit = ~bit_representation
    logical_value = bool(flipped_bit & 1)
    return logical_value

if __name__ == '__main__':
    true_val = True
    false_val = False
    result_for_true = invert_boolean_bitwise(true_val)
    result_for_false = invert_boolean_bitwise(false_val)
    print(result_for_true)
    print(result_for_false)