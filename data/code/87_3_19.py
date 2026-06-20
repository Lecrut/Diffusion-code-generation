def evaluate_expression(condition_a, condition_b, condition_c):
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    sample_condition_a = True
    sample_condition_b = False
    sample_condition_c = True
    
    if not isinstance(sample_condition_a, bool):
        raise ValueError("sample_condition_a must be a boolean")
    if not isinstance(sample_condition_b, bool):
        raise ValueError("sample_condition_b must be a boolean")
    if not isinstance(sample_condition_c, bool):
        raise ValueError("sample_condition_c must be a boolean")
    
    result = evaluate_expression(sample_condition_a, sample_condition_b, sample_condition_c)
    print(result)