import itertools
def generate_truth_table(A, B, C):
    combinations = list(itertools.product([0, 1], repeat=3))
    truth_table = []
    for a, b, c in combinations:
        row = [a, b, c]
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    A_val = 1
    B_val = 0
    C_val = 1
    truth_table_result = generate_truth_table(A_val, B_val, C_val)
    for row in truth_table_result:
        print(row)