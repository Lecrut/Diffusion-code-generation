def generate_truth_table(variables):
    n = len(variables)
    rows = []
    for i in range(2 ** n):
        row = {}
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            row[variables[j]] = bool(bit)
        rows.append(row)
    return rows

if __name__ == '__main__':
    vars_list = ['A', 'B']
    table = generate_truth_table(vars_list)
    for row in table:
        print(row)