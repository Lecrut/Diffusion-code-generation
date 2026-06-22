def evaluate_logic(A, B, C, D):
    return (A and B) or (C and not D)

if __name__ == '__main__':
    result = evaluate_logic(True, False, True, False)
    print(result)