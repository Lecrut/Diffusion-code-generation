def generate_truth_table(boolean_variables):
    num_vars = len(boolean_variables)
    truth_table = []

    for i in range(2 ** num_vars):
        combo = [(i >> j) & 1 for j in range(num_vars)]
        row = [combo]
        for var in boolean_variables:
            row.append(var(combo))
        truth_table.append(row)

    return truth_table

def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def not_gate(a):
    return not a

if __name__ == '__main__':
    variables = [and_gate, or_gate, not_gate]
    table = generate_truth_table(variables)
    for row in table:
        print(row)