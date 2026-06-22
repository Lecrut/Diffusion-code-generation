def generate_and_truth_table():
    inputs = [True, False]
    results = []
    for a in inputs:
        for b in inputs:
            results.append((a, b, a and b))
    return results

if __name__ == '__main__':
    table = generate_and_truth_table()
    for row in table:
        print(row)