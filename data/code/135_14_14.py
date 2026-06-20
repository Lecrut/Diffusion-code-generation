def evaluate_statements(stmt1, stmt2, values):
    for value in values:
        if eval(stmt1) != eval(stmt2):
            return False
    return True

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(evaluate_statements('x**2', 'x*x', sample_values))