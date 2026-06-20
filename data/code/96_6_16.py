TRUE = 1
FALSE = 0

def evaluate_expression(A: int, B: int, C: int, D: int) -> int:
    return (A & B) | (C & ~D)

if __name__ == '__main__':
    A = TRUE
    B = FALSE
    C = TRUE
    D = FALSE
    result = evaluate_expression(A, B, C, D)
    print(result)