def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    if len(sequence) < 2:
        raise ValueError("Input must contain at least two bits")
    
    input_bits = sequence[:-1]
    result_bit = sequence[-1]
    
    all_inputs_ones = all(bit == '1' for bit in input_bits)
    expected_result = '1' if all_inputs_ones else '0'
    
    return result_bit == expected_result

if __name__ == '__main__':
    print(check_and_operation("1111"))
    print(check_and_operation("1101"))
    print(check_and_operation("0000"))
    print(check_and_operation("1000"))