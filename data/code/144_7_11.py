import itertools

def build_truth_table(n):
    variables = [f'x{i}' for i in range(n)]
    truth_values = list(itertools.product([False, True], repeat=n))
    table = {vars: val for vars, val in zip(variables, truth_values)}
    return table

if __name__ == '__main__':
    n = 3
    truth_table = build_truth_table(n)
    print(truth_table)