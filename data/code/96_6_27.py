def evaluate_logic(A: int, B: int, C: int, D: int) -> int:
    return (A & B) | (C & ~D)

if __name__ == '__main__':
    try:
        A = 1
        B = 0
        C = 1
        D = 0
        result = evaluate_logic(A, B, C, D)
        print(result)
    except Exception as e:
        print(f"Error: {e}")