def generate_xor_truth_table():
    inputs = [0, 1]
    table = []
    for a in inputs:
        for b in inputs:
            result = a ^ b
            table.append((a, b, result))
    return table

if __name__ == '__main__':
    table = generate_xor_truth_table()
    for row in table:
        print(row)