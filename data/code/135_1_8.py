def truth_table(expr1, expr2):
    import itertools

    def evaluate(expr, values):
        for var, value in zip(variables, values):
            expr = expr.replace(var, str(value))
        return eval(expr)

    variables = set()
    for char in expr1 + expr2:
        if char.isalpha() and char.islower():
            variables.add(char)

    truth_values = list(itertools.product([False, True], repeat=len(variables)))
    results1 = [evaluate(expr1, values) for values in truth_values]
    results2 = [evaluate(expr2, values) for values in truth_values]

    return all(r1 == r2 for r1, r2 in zip(results1, results2))

if __name__ == '__main__':
    expr1 = "a and b"
    expr2 = "b and a"
    print(truth_table(expr1, expr2))