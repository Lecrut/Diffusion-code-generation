import itertools

def build_truth_table(n):
    variables = [f'P{i+1}' for i in range(n)]
    truth_values = list(itertools.product([False, True], repeat=n))
    table = {tuple(row): eval(' and '.join(f'{var} == {val}' for var, val in zip(variables, row))) for row in truth_values}
    return table

if __name__ == '__main__':
    n = 3
    truth_table = build_truth_table(n)
    print(truth_table)