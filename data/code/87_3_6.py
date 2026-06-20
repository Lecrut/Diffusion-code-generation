def evaluate_expression(condition_a, condition_b, condition_c):
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    sample_values = [
        (True, True, False),
        (False, False, True),
        (True, False, True),
        (False, True, False)
    ]
    
    for values in sample_values:
        result = evaluate_expression(*values)
        print(f"({values[0]} AND {values[1]}) OR {values[2]} = {result}")