def check_and_operation(sequence: str) -> bool:
    stripped = sequence.strip()
    if not stripped:
        raise ValueError("Input sequence cannot be empty")
    
    for char in stripped:
        if char not in ('0', '1'):
            raise ValueError(f"Invalid character '{char}' in sequence")
    
    if len(stripped) < 2:
        raise ValueError("Sequence must contain at least two bits")
    
    result_bit = stripped[-1]
    input_bits = stripped[:-1]
    
    all_inputs_one = all(bit == '1' for bit in input_bits)
    expected_result = '1' if all_inputs_one else '0'
    
    return result_bit == expected_result

if __name__ == '__main__':
    test_cases = [
        "111",
        "101",
        "011",
        "001",
        "110",
        "100"
    ]
    
    for case in test_cases:
        print(check_and_operation(case))