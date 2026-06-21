def truth_table(vars):
    n = len(vars)
    table = []
    for i in range(2**n):
        row = [bool(i & (1 << j)) for j in range(n)]
        row.append(all(row))
        table.append(row)
    return table

if __name__ == '__main__':
    vars = [True, False]
    print(truth_table(vars))