def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    parts = sequence.split(',')
    if len(parts) < 2:
        raise ValueError("Input must contain at least two values separated by commas")
    
    inputs = []
    for part in parts[:-1]:
        inputs.append(int(part))
    
    result = int(parts[-1])
    
    expected_result = 1
    for val in inputs:
        if val != 1:
            expected_result = 0
            break
    
    return result == expected_result

if __name__ == '__main__':
    print(check_and_operation("1,1,1"))
    print(check_and_operation("1,0,1"))
    print(check_and_operation("0,0,0"))