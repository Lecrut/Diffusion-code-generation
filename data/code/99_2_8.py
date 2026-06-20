def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        try:
            result = eval(expr)
            results.append((expr, result))
        except Exception as e:
            results.append((expr, str(e)))
    return results

if __name__ == '__main__':
    sample_expressions = [
        "3 + 4 * 2",
        "(10 / 3) * 2",
        "5 ** 2 - 3",
        "7 % 2 + 1"
    ]
    print(evaluate_expressions(sample_expressions))