def evaluate_statements(stmt1, stmt2, values):
    return all(eval(stmt1.format(x=x)) == eval(stmt2.format(x=x)) for x in values)

if __name__ == '__main__':
    print(evaluate_statements('(x + 1)', '(x - (-1))', range(-5, 6)))