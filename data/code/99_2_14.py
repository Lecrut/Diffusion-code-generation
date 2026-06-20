def evaluate_expressions(expressions):
    return [eval(expr) for expr in expressions]

if __name__ == '__main__':
    expressions = ['3 + 4 * 2', '8 / 2 ** 2', '5 - 3 + 1']
    results = evaluate_expressions(expressions)
    print(results)