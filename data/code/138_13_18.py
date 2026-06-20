def evaluate_boolean_operations(a, b):
    return (a and b), (a or b), not a, not b

if __name__ == '__main__':
    sample_values = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    
    for values in sample_values:
        print(evaluate_boolean_operations(*values))