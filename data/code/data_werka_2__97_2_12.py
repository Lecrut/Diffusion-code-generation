def generate_truth_table(inputs):
    n = len(inputs)
    rows = []
    for i in range(2 ** n):
        row = []
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            row.append(bool(bit))
        rows.append(row)
    
    header = " | ".join(inputs)
    print(header)
    print("-" * len(header))
    
    for row in rows:
        row_str = " | ".join(str(val) for val in row)
        print(row_str)

if __name__ == '__main__':
    generate_truth_table(["A", "B", "C"])