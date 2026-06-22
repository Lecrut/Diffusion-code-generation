def evaluate_logic(A, B, C, D):
    def to_bit(val):
        if val is None:
            raise ValueError("Input cannot be None")
        return 1 if val else 0

    a = to_bit(A)
    b = to_bit(B)
    c = to_bit(C)
    d = to_bit(D)

    term1 = a & b
    term2 = c & (1 ^ d)
    
    result = term1 | term2
    
    return result

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    result = evaluate_logic(A, B, C, D)
    print(result)