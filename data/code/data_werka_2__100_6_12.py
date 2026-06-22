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
            operands.append(True)
        else:
            operands.append(False)
    
    result = all(operands)
    
    expected_result = '1' if result else '0'
    
    if len(parts) > 2:
        last_part = parts[-1]
        if last_part != expected_result:
            return False
        return True
    
    return result

if __name__ == '__main__':
    test_sequences = [
        "1 1 1",
        "1 0 0",
        "0 0 0",
        "1 1 0"
    ]
    
    for seq in test_sequences:
        result = check_and_operation(seq)
        print(result)