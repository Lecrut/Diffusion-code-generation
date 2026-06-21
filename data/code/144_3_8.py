def truth_table(vars):
    n = len(vars)
    table = [[False] * (2 ** n) for _ in range(n)]
    for i in range(2 ** n):
        for j in range(n):
            table[j][i] = vars[j] == bool(i & (1 << j))
    return table

if __name__ == '__main__':
    sample_vars = [True, False]
    print(truth_table(sample_vars))