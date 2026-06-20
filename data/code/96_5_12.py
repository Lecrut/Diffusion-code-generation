TRUE = True
FALSE = False

def evaluate_expression(variables):
    A = variables['A']
    B = variables['B']
    C = variables['C']
    D = variables['D']
    return (A and B) or (C and not D)

if __name__ == '__main__':
    test_cases = [
        {'A': TRUE, 'B': FALSE, 'C': TRUE, 'D': FALSE},
        {'A': FALSE, 'B': TRUE, 'C': FALSE, 'D': TRUE},
        {'A': TRUE, 'B': TRUE, 'C': FALSE, 'D': FALSE},
        {'A': FALSE, 'B': FALSE, 'C': TRUE, 'D': TRUE}
    ]
    for case in test_cases:
        result = evaluate_expression(case)
        print(f"Input: {case} -> Output: {result}")