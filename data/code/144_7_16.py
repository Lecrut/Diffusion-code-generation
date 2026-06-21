import itertools

def build_truth_table(n):
    variables = [i for i in range(n)]
    truth_values = list(itertools.product([False, True], repeat=n))
    return {tuple(variables): values for variables, values in zip(itertools.permutations(variables), truth_values)}

if __name__ == '__main__':
    n = 3
    truth_table = build_truth_table(n)
    print(truth_table)