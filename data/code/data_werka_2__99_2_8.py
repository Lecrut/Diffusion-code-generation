def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        try:
            val = eval(expr)
            results.append((expr, val))
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
        "True and False or True",
        "1 + 2 + 3 * 4 ** 2"
    ]
    output = evaluate_expressions(sample_expressions)
    print(output)