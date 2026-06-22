def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    if len(sequence) < 2:
        raise ValueError("Input must contain at least two bits for an AND operation")
    
    input_bits = sequence[:-1]
    result_bit = sequence[-1]
    
    all_inputs_one = all(bit == '1' for bit in input_bits)
    expected_result = '1' if all_inputs_one else '0'
    
    return result_bit == expected_result

if __name__ == '__main__':
    test_sequence = "1111"
    result = check_and_operation(test_sequence)
    print(result)
    
    test_sequence_2 = "1101"
    result_2 = check_and_operation(test_sequence_2)
    print(result_2)
    
    test_sequence_3 = "0000"
    result_3 = check_and_operation(test_sequence_3)
    print(result_3)