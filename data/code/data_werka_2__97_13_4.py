def generate_and_truth_table(inputs):
    results = []
    for a in inputs:
        for b in inputs:
            results.append((a, b, a and b))
    return results

if __name__ == '__main__':
    sample_values = [True, False]
    truth_table = generate_and_truth_table(sample_values)
    for row in truth_table:
        print(row)