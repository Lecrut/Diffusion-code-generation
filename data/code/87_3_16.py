def evaluate_expression(condition_a: bool, condition_b: bool, condition_c: bool) -> bool:
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    sample_values = {
        'condition_a': True,
        'condition_b': False,
        'condition_c': True
    }
    
    result = evaluate_expression(**sample_values)
    print(result)