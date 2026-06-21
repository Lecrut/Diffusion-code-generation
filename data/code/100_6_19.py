def check_and_operation(sequence: str) -> bool:
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    length = len(sequence)
    if length < 2:
        return False
    
    inputs = sequence[:-1]
    result = sequence[-1]
    
    all_inputs_1 = all(bit == '1' for bit in inputs)
    expected_result = '1' if all_inputs_1 else '0'
    
    return result == expected_result

if __name__ == '__main__':
    test_sequence = "1111"
    output = check_and_operation(test_sequence)
    print(output)