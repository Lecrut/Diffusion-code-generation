import itertools

def build_truth_table(variables):
    n = len(variables)
    truth_values = list(itertools.product([False, True], repeat=n))
    table = {}
    for row in truth_values:
        key = tuple(row)
        values = {var: val for var, val in zip(variables, row)}
        table[key] = values
    return table

if __name__ == '__main__':
    variables = ["A", "B"]
    truth_table = build_truth_table(variables)
    print("Truth Table for A and B:")
    header = "|".join(f"{var:<3}" for var in variables)
    separator = "-" * len(header)
    print(header)
    print(separator)
    for key, values in truth_table.items():
        row = "|".join(f"{val:<3}" for val in values.values())
        print(row)