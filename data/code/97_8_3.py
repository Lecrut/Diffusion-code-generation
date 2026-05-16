def generate_truth_table(num_variables):
    num_rows = 2 ** num_variables
    truth_table = []
    for i in range(num_rows):
        row = []
        for j in range(num_variables):
            bit = (i >> j) & 1
            row.append(str(bit))
        truth_table.append(row)
    return truth_table
if __name__ == '__main__':
    num_vars = 3
    truth_table_data = generate_truth_table(num_vars)
    print(f"Truth Table for {num_vars} variables:")
    headers = []
    for i in range(num_vars):
        headers.append(f"V{i+1}")
    print(" | ".join(headers))
    print("-" * (len(headers) * 3 + len(headers) * 2))
    for row in truth_table_data:
        print(" | ".join(row))