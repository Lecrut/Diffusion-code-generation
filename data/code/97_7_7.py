def generate_truth_table(variables):
    n = len(variables)
    rows = []
    for i in range(2 ** n):
        row = []
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            row.append(bool(bit))
        rows.append(row)
    return variables, rows

if __name__ == '__main__':
    vars_list = ['A', 'B', 'C']
    variables, rows = generate_truth_table(vars_list)
    print(variables)
    for row in rows:
        print(row)