def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    parts = sequence.split()
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two operands separated by space")
    
    operand_a = parts[0]
    operand_b = parts[1]
    
    if len(operand_a) != len(operand_b):
        raise ValueError("Operands must have the same length")
    
    result = []
    for i in range(len(operand_a)):
        bit_a = operand_a[i]
        bit_b = operand_b[i]
        if bit_a == '1' and bit_b == '1':
            result.append('1')
        else:
            result.append('0')
    
    computed_result = ''.join(result)
    
    if len(parts) == 3:
        expected_result = parts[2]
        if len(expected_result) != len(computed_result):
            raise ValueError("Result length mismatch")
        return computed_result == expected_result
    else:
        return computed_result

if __name__ == '__main__':
    print(check_and_operation("1 1 1"))
    print(check_and_operation("1 0 0"))
    print(check_and_operation("11 10 10"))
    print(check_and_operation("101 111 101"))