def generate_truth_table(variables):
    n = len(variables)
    rows = []
    for i in range(2 ** n):
        row = {}
        for j in range(n):
            row[variables[j]] = bool((i >> (n - 1 - j)) & 1)
        rows.append(row)
    return rows

if __name__ == '__main__':
    vars_list = ['A', 'B']
    result = generate_truth_table(vars_list)
    print(result)