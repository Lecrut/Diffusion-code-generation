def evaluate_with_precedence(expressions):
    results = {}
    for expr in expressions:
        try:
            result = eval(expr)
            results[expr] = result
        except Exception as e:
            results[expr] = f"Error: {e}"
    return results
if __name__ == '__main__':
    sample_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "5 + 6 / 2 - 1",
        "10 / 2 + 5 * 3",
        "8 - 2 * 3 + 4"
    ]
    evaluation_results = evaluate_with_precedence(sample_expressions)
    for expression, result in evaluation_results.items():
        print(f"Expression: '{expression}'")
        print(f"Result: {result}\n")