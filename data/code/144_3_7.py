def truth_table(vars):
    if not vars:
        return [[]]
    first_var = vars[0]
    rest_vars = vars[1:]
    table = []
    for val in [False, True]:
        sub_table = truth_table(rest_vars)
        for row in sub_table:
            table.append([val] + row)
    return table

if __name__ == '__main__':
    print(truth_table([True, False]))