def evaluate_expression(variables):
    result = (variables['A'] and variables['B']) or (variables['C'] and not variables['D'])
    return result

if __name__ == '__main__':
    test_cases = [
        {'A': True, 'B': False, 'C': True, 'D': True},
        {'A': False, 'B': False, 'C': False, 'D': True},
        {'A': True, 'B': True, 'C': False, 'D': False}
    ]
    
    for case in test_cases:
        print(evaluate_expression(case))