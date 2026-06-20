TRUE = 1
FALSE = 0

def evaluate_logic(a, b, c, d):
    return a & b | c & ~d
if __name__ == '__main__':
    A = TRUE
    B = FALSE
    C = TRUE
    D = FALSE
    result = evaluate_logic(A, B, C, D)
    print(result)