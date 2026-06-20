def evaluate_statements(stmt1, stmt2, values):
    return all(eval(stmt1.format(x=x)) == eval(stmt2.format(x=x)) for x in values)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(evaluate_statements('(x**2)', '(x*x)', sample_values))