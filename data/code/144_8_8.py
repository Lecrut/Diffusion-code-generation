import itertools
def generate_truth_table(num_vars):
    num_rows = 2**num_vars
    truth_table = []
    indices = range(num_rows)
    for i in indices:
        row = []
        for j in range(num_vars):
            bit = (i >> j) & 1
            row.append(str(bit))
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    num_vars = 3
    truth_table_data = generate_truth_table(num_vars)
    print(f"Truth Table for {num_vars} variables:")
    headers = [f"V{i+1}" for i in range(num_vars)]
    print(" | ".join(headers))
    print("-" * (len(headers) * 3 + (len(headers) - 1)))
    for row in truth_table_data:
        print(" | ".join(row))