import itertools

def generate_truth_table(variables):
    num_vars = len(variables)
    combinations = itertools.product([False, True], repeat=num_vars)
    rows = []
    for combo in combinations:
        row = {var: val for var, val in zip(variables, combo)}
        rows.append(row)
    return rows

if __name__ == '__main__':
    vars_list = ['A', 'B', 'C']
    table = generate_truth_table(vars_list)
    for row in table:
        print(row)