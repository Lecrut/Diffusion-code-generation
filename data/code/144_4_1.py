def generate_truth_table(A, B, C):
    rows = []
    for i in range(8):
        a = (i >> 2) & 1
        b = (i >> 1) & 1
        c = (i >> 0) & 1
        rows.append((a, b, c))
    return rows
if __name__ == '__main__':
    A_val = 1
    B_val = 0
    C_val = 1
    truth_table = generate_truth_table(A_val, B_val, C_val)
    for row in truth_table:
        print(row)