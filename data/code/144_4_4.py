def generate_truth_table(A, B, C):
    results = []
    for i in range(8):
        a = (i >> 2) & 1
        b = (i >> 1) & 1
        c = (i >> 0) & 1
        result = (a << 2) | (b << 1) | c
        results.append(result)
    return results
if __name__ == '__main__':
    A_val = 1
    B_val = 0
    C_val = 1
    truth_table = generate_truth_table(A_val, B_val, C_val)
    print(f"Input: A={A_val}, B={B_val}, C={C_val}")
    print("Truth Table Rows (Decimal):")
    for row in truth_table:
        print(row)
    print("\nTruth Table Rows (Binary):")
    for row in truth_table:
        print(row)