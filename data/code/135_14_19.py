def check_equivalence(stmt1, stmt2, values):
    return all(eval(stmt1, {}, {**locals(), **values}) == eval(stmt2, {}, {**locals(), **values}) for value in values)

if __name__ == '__main__':
    sample_values = {'x': 1, 'y': 2}
    print(check_equivalence('x + y', 'y + x', sample_values))