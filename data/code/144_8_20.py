def evaluate_expression(variables):
    A, B, C, D = map(int, variables)
    return (A or B) and (C or D)

if __name__ == '__main__':
    sample_values = [
        ('0000', 'False'),
        ('0001', 'True'),
        ('0010', 'True'),
        ('0011', 'True'),
        ('0100', 'True'),
        ('0101', 'True'),
        ('0110', 'True'),
        ('0111', 'True'),
        ('1000', 'False'),
        ('1001', 'True'),
        ('1010', 'True'),
        ('1011', 'True'),
        ('1100', 'True'),
        ('1101', 'True'),
        ('1110', 'True'),
        ('1111', 'True')
    ]
    
    for input_val, expected_output in sample_values:
        result = evaluate_expression(input_val)
        assert str(result) == expected_output, f"Test failed for input {input_val}. Expected {expected_output}, got {result}"
    
    print("All tests passed!")