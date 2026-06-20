def are_statements_equivalent(stmt1, stmt2, values):
    return all(eval(stmt1) == eval(stmt2) for value in values)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(are_statements_equivalent('x**2', 'x*x', sample_values))