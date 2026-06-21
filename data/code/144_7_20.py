import itertools

def build_truth_table(n):
    VARIABLES = [f'x{i}' for i in range(n)]
    TRUTH_VALUES = list(itertools.product([False, True], repeat=n))
    
    def evaluate_expression(row):
        expression = ' and '.join(f'{var} == {val}' for var, val in zip(VARIABLES, row))
        return eval(expression)
    
    truth_table = {tuple(row): evaluate_expression(row) for row in TRUTH_VALUES}
    return truth_table

if __name__ == '__main__':
    n = 3
    truth_table = build_truth_table(n)
    print(truth_table)