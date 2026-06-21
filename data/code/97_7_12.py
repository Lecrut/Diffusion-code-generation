import itertools

def generate_truth_table(variables):
    num_vars = len(variables)
    rows = []
    for combination in itertools.product([False, True], repeat=num_vars):
        row = dict(zip(variables, combination))
        rows.append(row)
    return rows

if __name__ == '__main__':
    vars_list = ['A', 'B', 'C']
    table = generate_truth_table(vars_list)
    for row in table:
        print(row)