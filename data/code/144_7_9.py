import itertools

def build_truth_table(n):
    variables = [f'x{i}' for i in range(n)]
    combinations = list(itertools.product([False, True], repeat=n))
    truth_table = {tuple(row): eval(' and '.join(f'{var} == {val}' for var, val in zip(variables, row))) for row in combinations}
    return truth_table

if __name__ == '__main__':
    sample_truth_table = build_truth_table(3)
    print(sample_truth_table)