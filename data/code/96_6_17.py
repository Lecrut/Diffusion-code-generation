def evaluate_logic(a: int, b: int, c: int, d: int) -> int:
    return (a & b) | (c & ~d)

if __name__ == '__main__':
    A = 1
    B = 0
    C = 1
    D = 0
    
    result = evaluate_logic(A, B, C, D)
    print(result)