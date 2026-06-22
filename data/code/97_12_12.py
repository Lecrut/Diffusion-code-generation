def generate_xor_truth_table():
    table = []
    for a in [0, 1]:
        for b in [0, 1]:
            result = a ^ b
            table.append((a, b, result))
    return table

if __name__ == '__main__':
    table = generate_xor_truth_table()
    for row in table:
        print(row)