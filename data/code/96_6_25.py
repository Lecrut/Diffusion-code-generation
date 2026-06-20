def validate_inputs(A, B, C, D):
    if not all(isinstance(x, int) for x in [A, B, C, D]):
        raise ValueError("All inputs must be integers")
    if A != 0 and A != 1:
        raise ValueError("A must be either 0 or 1")
    if B != 0 and B != 1:
        raise ValueError("B must be either 0 or 1")
    if C != 0 and C != 1:
        raise ValueError("C must be either 0 or 1")
    if D != 0 and D != 1:
        raise ValueError("D must be either 0 or 1")

def evaluate_expression(A, B, C, D):
    validate_inputs(A, B, C, D)
    return (A & B) | (C & ~D)

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    result = evaluate_expression(A, B, C, D)
    print(result)