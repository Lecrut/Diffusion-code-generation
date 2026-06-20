def validate_inputs(a, b, c, d):
    if not all(isinstance(x, bool) for x in [a, b, c, d]):
        raise ValueError("All inputs must be boolean values.")
    
def evaluate_nested_logic(a, b, c, d):
    validate_inputs(a, b, c, d)
    return (a and b) or (c and not d)

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    result = evaluate_nested_logic(A, B, C, D)
    print(result)