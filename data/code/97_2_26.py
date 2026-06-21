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
        print(" | ".join(str(x) for x in row))

if __name__ == '__main__':
    inputs = ["A", "B"]
    generate_truth_table(inputs)