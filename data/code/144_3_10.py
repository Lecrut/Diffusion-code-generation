def generate_truth_table(boolean_vars):
    num_vars = len(boolean_vars)
    truth_table = []
    for i in range(2 ** num_vars):
        row = [bool(i >> j & 1) for j in range(num_vars)]
        truth_table.append(row + [all(row)])
    return truth_table

if __name__ == '__main__':
    sample_values = [True, False]
    print(generate_truth_table(sample_values))