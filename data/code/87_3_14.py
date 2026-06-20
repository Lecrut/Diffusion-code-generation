def evaluate_expression(condition_a, condition_b, condition_c):
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    sample_values = [
        (True, True, True),
        (False, False, True),
        (True, False, False),
        (False, True, False)
    ]
    
    for a, b, c in sample_values:
        result = evaluate_expression(a, b, c)
        print(f"({a} AND {b}) OR {c}: {result}")