def analyze_expression_precedence(expressions):
    results = []
    for expr in expressions:
        val = eval(expr)
        results.append((expr, val))
    return results

if __name__ == '__main__':
    sample_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2 ** 3 ** 2",
        "10 / 3 + 1",
        "10 // 3 + 1"
    ]
    print(analyze_expression_precedence(sample_expressions))