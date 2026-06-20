TRUE = True
FALSE = False

def evaluate_nested_logic(a, b, c, d):
    return a and b or (c and (not d))
if __name__ == '__main__':
    A = TRUE
    B = FALSE
    C = TRUE
    D = FALSE
    result = evaluate_nested_logic(A, B, C, D)
    print(result)