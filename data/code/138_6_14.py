def generate_truth_table():
    truth_values = [False, True]
    results = []

    for A in truth_values:
        for B in truth_values:
            implication_result = not A or B
            equivalence_result = A == B
            results.append((A, B, implication_result, equivalence_result))

    return results

if __name__ == '__main__':
    sample_results = generate_truth_table()
    print(sample_results)