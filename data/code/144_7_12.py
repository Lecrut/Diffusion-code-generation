import itertools

def build_truth_table(n):
    variables = [f'x{i}' for i in range(n)]
    values = list(itertools.product([False, True], repeat=n))
    truth_table = {var: [] for var in variables}
    
    for value in values:
        for i, var in enumerate(variables):
            truth_table[var].append(value[i])
    
    return truth_table

if __name__ == '__main__':
    n = 3
    table = build_truth_table(n)
    print(table)