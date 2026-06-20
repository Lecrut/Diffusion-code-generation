def generate_truth_table(vars):
    table = []
    n_vars = len(vars)
    
    def helper(index=0):
        if index == n_vars:
            table.append([vars[i][v] for i, v in enumerate(var_values)])
            return
        for val in [0, 1]:
            var_values[index] = val
            helper(index + 1)

    var_values = [None] * n_vars
    helper()
    return table

if __name__ == '__main__':
    vars = [
        ("A", [0, 1]),
        ("B", [0, 1]),
        ("C", [0, 1]),
        ("D", [0, 1])
    ]
    truth_table = generate_truth_table(vars)
    for row in truth_table:
        print(row)