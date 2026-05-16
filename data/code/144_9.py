def generate_truth_table(n):
    num_rows = 2**n
    truth_table = []
    for i in range(num_rows):
        row = []
        for j in range(n):
            bit = (i >> j) & 1
            row.append(str(bit))
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    N = 3
    truth_table_data = generate_truth_table(N)
    for row in truth_table_data:
        print(" ".join(row))