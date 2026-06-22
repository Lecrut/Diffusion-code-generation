def generate_xor_truth_table():
    inputs = [0, 1]
    results = []
    for a in inputs:
        for b in inputs:
            output = a ^ b
            results.append((a, b, output))
    return results

if __name__ == '__main__':
    table = generate_xor_truth_table()
    for row in table:
        print(row)