def evaluate_logic(A, B, C, D):
    return (A & B) | (C & ~D)

if __name__ == '__main__':
    print(evaluate_logic(1, 0, 1, 0))