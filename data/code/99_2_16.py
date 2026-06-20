def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        result = eval(expr)
        results.append((expr, result))
    return results

if __name__ == '__main__':
    sample_expressions = [
        "3 + 4 * 2",
        "(10 / 3) ** 2",
        "5 % 2 + 3 // 2"
    ]
    print(evaluate_expressions(sample_expressions))