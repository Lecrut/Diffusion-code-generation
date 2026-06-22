def check_and_operation(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    
    for char in sequence:
        if char not in ('0', '1'):
            raise ValueError("Input must contain only '0' and '1'")
    
    parts = sequence.split()
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two operands separated by space")
    
    operand1 = parts[0]
    operand2 = parts[1]
    
    if len(operand1) != len(operand2):
        raise ValueError("Operands must have the same length")
    
    result = []
    for i in range(len(operand1)):
        bit1 = operand1[i]
        bit2 = operand2[i]
        if bit1 == '1' and bit2 == '1':
            result.append('1')
        else:
            result.append('0')
    
    return ''.join(result)

if __name__ == '__main__':
    sequence1 = "1 1"
    sequence2 = "1 0"
    sequence3 = "0 1"
    sequence4 = "0 0"
    
    print(check_and_operation(sequence1))
    print(check_and_operation(sequence2))
    print(check_and_operation(sequence3))
    print(check_and_operation(sequence4))