def truth_table(booleans):
    from itertools import product

    headers = [''] + [f'x{i+1}' for i in range(len(booleans))]
    rows = list(product([False, True], repeat=len(booleans)))
    table = [headers] + [[row[i] for i in range(len(row))] + [all(row[:i+1])] for row in rows]
    return table

if __name__ == '__main__':
    sample_booleans = [True, False, True]
    print(truth_table(sample_booleans))