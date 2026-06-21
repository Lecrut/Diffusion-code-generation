import itertools

def evaluate_expression(A, B, C):
    return (A and B) or not C

def generate_truth_table():
    variables = ['A', 'B', 'C']
    combinations = list(itertools.product([False, True], repeat=len(variables)))
    truth_table = [(tuple(comb), evaluate_expression(*comb)) for comb in combinations]
    return truth_table

if __name__ == '__main__':
    sample_values = generate_truth_table()
    print(sample_values)