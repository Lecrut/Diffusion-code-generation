def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    parts = sequence.split()
    if len(parts) < 2:
        raise ValueError("Input must contain at least two operands")
    
    operands = []
    for part in parts:
        if part == '1':
            operands.append(1)
        else:
            operands.append(0)
    
    result = 1
    for op in operands:
        result = result & op
    
    return result == 1

if __name__ == '__main__':
    test_sequence = "1 1 1"
    result = check_and_operation(test_sequence)
    print(result)
    
    test_sequence_2 = "1 0 1"
    result_2 = check_and_operation(test_sequence_2)
    print(result_2)