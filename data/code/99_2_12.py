def evaluate_expressions(expressions):
    return [eval(expr) for expr in expressions]

if __name__ == '__main__':
    sample_expressions = ["3 + 4 * 2", "5 / (7 - 2)", "(10 + 2) * 3"]
    results = evaluate_expressions(sample_expressions)
    print(results)