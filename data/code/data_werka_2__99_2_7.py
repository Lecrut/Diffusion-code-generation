def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        try:
            value = eval(expr)
            results.append((expr, value))
        except Exception:
            results.append((expr, None))
    return results

if __name__ == '__main__':
    sample_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2 ** 3 ** 2",
        "10 / 3 + 2",
        "10 // 3 + 2",
        "2 + 2 * 2 ** 2",
        "1 + 2 + 3 * 4 - 5",
        "10 % 3 + 2",
        "2 * 3 + 4 * 5",
        "10 - 5 + 2"
    ]
    output = evaluate_expressions(sample_expressions)
    for expr, val in output:
        print(f"{expr} = {val}")