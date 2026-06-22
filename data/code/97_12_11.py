def generate_xor_truth_table():
    results = []
    for a in [0, 1]:
        for b in [0, 1]:
            output = a ^ b
            results.append((a, b, output))
    return results

if __name__ == '__main__':
    table = generate_xor_truth_table()
    for row in table:
        print(row)