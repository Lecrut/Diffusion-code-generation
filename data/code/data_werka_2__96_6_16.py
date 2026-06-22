TRUE_MASK = 1
FALSE_MASK = 0

def evaluate_logic(A, B, C, D):
    a_bit = 1 if A else 0
    b_bit = 1 if B else 0
    c_bit = 1 if C else 0
    d_bit = 1 if D else 0
    not_d_bit = 1 if not d_bit else 0
    term1 = a_bit & b_bit
    term2 = c_bit & not_d_bit
    result = term1 | term2
    return result

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    result = evaluate_logic(A, B, C, D)
    print(result)