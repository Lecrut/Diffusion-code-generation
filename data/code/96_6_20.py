def evaluate_logic(a, b, c, d):
    return (a & b) | (c & ~d)

if __name__ == '__main__':
    try:
        A = 1
        B = 0
        C = 1
        D = 0
        result = evaluate_logic(A, B, C, D)
        print(result)
    except TypeError as e:
        print(f"Invalid input: {e}")