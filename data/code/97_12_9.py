def generate_xor_truth_table():
    inputs = [0, 1]
    table = []
    for a in inputs:
        for b in inputs:
            output = a ^ b
            table.append((a, b, output))
    return table

if __name__ == '__main__':
    result = generate_xor_truth_table()
    for row in result:
        print(row)