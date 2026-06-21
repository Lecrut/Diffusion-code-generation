import itertools

def build_truth_table(n):
    variables = [f'x{i}' for i in range(n)]
    truth_table = list(itertools.product([False, True], repeat=n))
    return {tuple(row): eval(' and '.join(f'{var} == {value}' for var, value in zip(variables, row))) for row in truth_table}

if __name__ == '__main__':
    n = 3
    table = build_truth_table(n)
    print(table)