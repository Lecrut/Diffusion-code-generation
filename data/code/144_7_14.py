import itertools

def generate_truth_table(variables):
    n = len(variables)
    if not all((isinstance(var, str) and var.isalpha() for var in variables)):
        raise ValueError('All variable names must be strings consisting of alphabetic characters.')
    combinations = list(itertools.product([False, True], repeat=n))
    header = ' | '.join(variables)
    print(header)
    print('-' * len(header))
    for combination in combinations:
        row = ' | '.join(map(str, combination))
        print(row)
if __name__ == '__main__':
    variables = ['A', 'B']
    generate_truth_table(variables)