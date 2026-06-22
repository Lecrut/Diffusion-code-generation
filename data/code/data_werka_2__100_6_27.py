def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    length = len(sequence)
    if length < 2:
        raise ValueError("Input must contain at least two bits for an AND operation")
    
    inputs = sequence[:-1]
    result = sequence[-1]
    
    all_inputs_one = all(bit == '1' for bit in inputs)
    expected_result = '1' if all_inputs_one else '0'
    
    return result == expected_result

if __name__ == '__main__':
    test_sequences = [
        "111",
        "101",
        "000",
        "110",
        "11111"
    ]
    
    for seq in test_sequences:
        is_valid = check_and_operation(seq)
        print(f"{seq}: {is_valid}")