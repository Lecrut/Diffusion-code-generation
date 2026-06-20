def evaluate_expression(condition_a, condition_b, condition_c):
    return (condition_a and condition_b) or condition_c

if __name__ == '__main__':
    sample_values = [
        (True, False, True),
        (False, True, False),
        (True, True, False),
        (False, False, True)
    ]
    
    for values in sample_values:
        result = evaluate_expression(*values)
        print(f"Condition A: {values[0]}, Condition B: {values[1]}, Condition C: {values[2]} -> Result: {result}")