def truth_table(expr1, expr2):
    import itertools

    def evaluate(expression, values):
        for var, value in values.items():
            expression = expression.replace(var, str(value).lower())
        return eval(expression)

    variables = set(expr1) & set(expr2)
    variables = {var for var in variables if var.isalpha()}
    truth_values = list(itertools.product([False, True], repeat=len(variables)))

    results1 = [evaluate(expr1, dict(zip(variables, values))) for values in truth_values]
    results2 = [evaluate(expr2, dict(zip(variables, values))) for values in truth_values]

    return all(r1 == r2 for r1, r2 in zip(results1, results2))

if __name__ == '__main__':
    expr1 = "a and b"
    expr2 = "b and a"
    print(truth_table(expr1, expr2))