def truth_table(expr1, expr2):
    import itertools

    def evaluate(expression, values):
        for var, value in values.items():
            expression = expression.replace(var, str(value))
        return eval(expression)

    variables = set()
    for char in expr1 + expr2:
        if char.isalpha() and char.islower():
            variables.add(char)

    truth_values = list(itertools.product([False, True], repeat=len(variables)))
    variable_dict = {var: values[i] for i, var in enumerate(variables)}

    results = []
    for values in truth_values:
        result1 = evaluate(expr1, variable_dict)
        result2 = evaluate(expr2, variable_dict)
        results.append((values, result1 == result2))

    return all(result[1] for result in results)

if __name__ == '__main__':
    expr1 = "a and b"
    expr2 = "b and a"
    print(truth_table(expr1, expr2))