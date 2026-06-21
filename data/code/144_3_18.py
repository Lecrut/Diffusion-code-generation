def generate_truth_table(booleans):
    from itertools import product

    num_vars = len(booleans)
    truth_values = list(product([False, True], repeat=num_vars))
    truth_table = []

    for values in truth_values:
        row = []
        for var, value in zip(booleans, values):
            row.append(value if var else not value)
        truth_table.append(row)

    return truth_table

if __name__ == '__main__':
    sample_booleans = [True, False]
    print(generate_truth_table(sample_booleans))