def evaluate_logic(A, B, C, D):
    return (A & B) | (C & ~D)

if __name__ == '__main__':
    sample_values = {'A': 1, 'B': 0, 'C': 1, 'D': 0}
    A = sample_values['A']
    B = sample_values['B']
    C = sample_values['C']
    D = sample_values['D']
    result = evaluate_logic(A, B, C, D)
    print(result)