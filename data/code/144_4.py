def generate_truth_table(A, B, C):
    results = []
    for i in range(8):
        a = (i >> 2) & 1
        b = (i >> 1) & 1
        c = (i >> 0) & 1
        val_a = 'T' if a == 1 else 'F'
        val_b = 'T' if b == 1 else 'F'
        val_c = 'T' if c == 1 else 'F'
        results.append((val_a, val_b, val_c))
    return results
if __name__ == '__main__':
    A_val = 1
    B_val = 0
    C_val = 1
    truth_table = generate_truth_table(A_val, B_val, C_val)
    for row in truth_table:
        print(row)