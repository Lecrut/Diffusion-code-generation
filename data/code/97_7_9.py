def generate_truth_table(num_vars):
    if num_vars < 1:
        raise ValueError("Number of variables must be at least 1")
    
    rows = []
    for i in range(2 ** num_vars):
        row = []
        for j in range(num_vars - 1, -1, -1):
            bit = (i >> j) & 1
            row.append(bool(bit))
        rows.append(row)
    
    headers = [f"p{i+1}" for i in range(num_vars)]
    return headers, rows

if __name__ == '__main__':
    headers, rows = generate_truth_table(3)
    print(headers)
    for row in rows:
        print(row)