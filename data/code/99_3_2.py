import operator
def evaluate_expression_with_precedence(expressions):
    results = {}
    for expr in expressions:
        tokens = expr.split()
        if not tokens:
            results[expr] = "Error: Empty expression"
            continue
        evaluated_tokens = []
        for i, token in enumerate(tokens):
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                evaluated_tokens.append(float(token))
            elif token in "+-*/^()":
                evaluated_tokens.append(token)
            else:
                results[expr] = f"Error: Invalid token '{token}'"
                break
        else:
            try:
                result = eval(expr)
                results[expr] = result
            except Exception as e:
                results[expr] = f"Evaluation Error: {e}"
    return results
if __name__ == '__main__':
    sample_expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "5 + 6 - 2",
        "10 / 2 + 5 * 3",
        "2 ^ 3 ^ 2",
        "10 * (2 + 3) / 5"
    ]
    evaluation_results = evaluate_expression_with_precedence(sample_expressions)
    for expr, result in evaluation_results.items():
        print(f"Expression: '{expr}' -> Result: {result}")