def generate_truth_table(variables):
    num_vars = len(variables)
    for i in range(2 ** num_vars):
        row = []
        for j in range(num_vars):
            row.append(bool(i & (1 << j)))
        print(row)

if __name__ == '__main__':
    variables = ['A', 'B', 'C']
    generate_truth_table(variables)