import itertools

def build_truth_table(variables):
    if not all(isinstance(var, str) and var.isalpha() for var in variables):
        raise ValueError("All variable names must be strings consisting of alphabetic characters.")
    
    n = len(variables)
    truth_values = list(itertools.product([False, True], repeat=n))
    header = ' | '.join(variables)
    print(header)
    print('-' * len(header))
    for row in truth_values:
        print(' | '.join(map(str, row)))

if __name__ == '__main__':
    variables = ["A", "B"]
    build_truth_table(variables)