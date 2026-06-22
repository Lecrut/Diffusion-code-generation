def check_and_operation(sequence):
    if not sequence:
        return False
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    if len(sequence) < 2:
        return False
    input_bits = sequence[:-1]
    result_bit = sequence[-1]
    all_inputs_one = all(bit == '1' for bit in input_bits)
    expected_result = '1' if all_inputs_one else '0'
    return result_bit == expected_result

if __name__ == '__main__':
    test_sequence = "111"
    result = check_and_operation(test_sequence)
    print(result)
    
    test_sequence_invalid = "110"
    result_invalid = check_and_operation(test_sequence_invalid)
    print(result_invalid)
    
    test_sequence_zeros = "000"
    result_zeros = check_and_operation(test_sequence_zeros)
    print(result_zeros)