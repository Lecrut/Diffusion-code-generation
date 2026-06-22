def generate_xor_truth_table():
    rows = []
    for a in [0, 1]:
        for b in [0, 1]:
            result = a ^ b
            rows.append((a, b, result))
    return rows

if __name__ == '__main__':
    table = generate_xor_truth_table()
    for a, b, result in table:
        print(f"{a} XOR {b} = {result}")