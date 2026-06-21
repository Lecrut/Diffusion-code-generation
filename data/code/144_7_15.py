import itertools

def build_truth_table(variables):
    n = len(variables)
    truth_values = list(itertools.product([False, True], repeat=n))
    table = []
    for row in truth_values:
        table.append(list(row))
    return table

if __name__ == '__main__':
    variables = ["X", "Y", "Z"]
    truth_table = build_truth_table(variables)
    header = ' | '.join(variables)
    print(header)
    print("-" * len(header))
    for row in truth_table:
        print(' | '.join(str(bit) for bit in row))