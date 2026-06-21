def evaluate_expressions(expressions):
    results = []
    for expr in expressions:
        try:
            result = eval(expr)
            results.append((expr, result))
        except Exception as e:
            results.append((expr, f"Error: {e}"))
    return results

if __name__ == '__main__':
    sample_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2 ** 3 ** 2",
        "10 / 3 + 2",
        "10 // 3 + 2"
    ]
    output = evaluate_expressions(sample_expressions)
    print(output)