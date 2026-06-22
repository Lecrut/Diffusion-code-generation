def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    parts = sequence.split(',')
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two values separated by a comma")
    
    input1 = parts[0].strip()
    input2 = parts[1].strip()
    
    if input1 not in ('0', '1') or input2 not in ('0', '1'):
        raise ValueError("Inputs must be '0' or '1'")
    
    result = '1' if (input1 == '1' and input2 == '1') else '0'
    
    return result == input2

if __name__ == '__main__':
    test_cases = [
        "1,1",
        "1,0",
        "0,1",
        "0,0"
    ]
    
    for case in test_cases:
        result = check_and_operation(case)
        print(f"{case} -> {result}")