def compute_truth_table(A, B, C):
    truth_row = []
    truth_row.append((A and B) or not C)
    return truth_row

if __name__ == '__main__':
    sample_A = True
    sample_B = False
    sample_C = True
    result = compute_truth_table(sample_A, sample_B, sample_C)
    print("A | B | C | (A AND B) OR (NOT C)")
    print(f"{sample_A} | {sample_B} | {sample_C} | {result[0]}")