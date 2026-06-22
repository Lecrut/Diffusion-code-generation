def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        try:
            result = eval(expr)
            results.append((expr, result))
        except Exception:
            results.append((expr, None))
    return results

if __name__ == '__main__':
    sample_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 / 2 + 3",
        "10 / (2 + 3)",
        "2 ** 3 ** 2",
        "2 ** (3 ** 2)",
        "1 + 2 + 3 * 4 - 5",
        "10 % 3 + 2",
        "10 // 3 + 2",
        "True and False or True"
    ]
    output = evaluate_expressions(sample_expressions)
    for expr, val in output:
        print(f"{expr} = {val}")