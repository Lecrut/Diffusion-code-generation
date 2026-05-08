import itertools
def generate_truth_table(A, B, C):
    results = []
    for a in range(8):
        row = [a & 1, a >> 1 & 1, a >> 2 & 1]
        results.append(row)
    return results
if __name__ == '__main__':
    A_val = 1
    B_val = 0
    C_val = 1
    truth_table = generate_truth_table(A_val, B_val, C_val)
    print(f"Input A={A_val}, B={B_val}, C={C_val}")
    for row in truth_table:
        print(row)