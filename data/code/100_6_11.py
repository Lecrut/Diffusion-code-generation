def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    length = len(sequence)
    if length < 2:
        raise ValueError("Input must contain at least two bits")
    
    inputs = sequence[:-1]
    result = sequence[-1]
    
    all_inputs_one = True
    for bit in inputs:
        if bit != '1':
            all_inputs_one = False
            break
    
    expected_result = '1' if all_inputs_one else '0'
    
    return result == expected_result

if __name__ == '__main__':
    test_sequence = "1111"
    output = check_and_operation(test_sequence)
    print(output)
    
    test_sequence_2 = "1011"
    output_2 = check_and_operation(test_sequence_2)
    print(output_2)
    
    test_sequence_3 = "1110"
    output_3 = check_and_operation(test_sequence_3)
    print(output_3)