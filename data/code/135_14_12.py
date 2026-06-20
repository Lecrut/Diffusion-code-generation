def are_equivalent_statements(stmt1, stmt2, values):
    return all(eval(stmt1) == eval(stmt2) for val in values)

if __name__ == '__main__':
    sample_values = [0, 1, -1, 2, -2]
    print(are_equivalent_statements('x**2', 'x*x', sample_values))