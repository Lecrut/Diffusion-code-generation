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
    truth_table_data = []
    num_rows = 2**N
    for i in range(num_rows):
        row = [str((i >> j) & 1) for j in range(N)]
        truth_table_data.append(row)
    print(f"Truth Table for N={N}:")
    header = [f"V{j+1}" for j in range(N)]
    print(" | ".join(header))
    for row in truth_table_data:
        print(" | ".join(row))