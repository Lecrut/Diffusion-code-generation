def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        result = eval(expr)
        results.append((expr, result))
    return results

if __name__ == '__main__':
    expressions = [
        "3 + 4 * 2",
        "(1 + 2) * (3 + 4)",
        "10 / 2 - 5",
        "2 ** 3 + 4"
    ]
    results = evaluate_expressions(expressions)
    for expr, result in results:
        print(f"{expr} -> {result}")