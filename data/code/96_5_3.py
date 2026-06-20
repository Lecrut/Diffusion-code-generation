def evaluate_expression(variables):
    return (variables['A'] and variables['B']) or (variables['C'] and not variables['D'])

if __name__ == '__main__':
    test_cases = [
        {'A': True, 'B': False, 'C': True, 'D': False},
        {'A': False, 'B': True, 'C': False, 'D': True},
        {'A': True, 'B': True, 'C': False, 'D': False},
        {'A': False, 'B': False, 'C': True, 'D': True}
    ]
    
    for case in test_cases:
        result = evaluate_expression(case)
        print(f"Input: {case} -> Output: {result}")