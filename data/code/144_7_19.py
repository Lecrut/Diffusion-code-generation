import itertools

def generate_truth_table(n):
    variables = [f'v{i}' for i in range(n)]
    truth_values = list(itertools.product([False, True], repeat=n))
    table = {tuple(row): eval(' and '.join(f'{var} == {val}' for var, val in zip(variables, row))) for row in truth_values}
    return table

if __name__ == '__main__':
    sample_truth_table = generate_truth_table(3)
    print(sample_truth_table)