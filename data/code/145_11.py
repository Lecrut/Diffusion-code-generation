def evaluate_nested_logic(inputs, expressions):
    results = {}
    for expr in expressions:
        try:
            evaluated_expr = eval(expr, {"__builtins__": None}, inputs)
            results[expr] = bool(evaluated_expr)
        except Exception:
            results[expr] = None
    return results
if __name__ == '__main__':
    boolean_inputs = {
        "A": True,
        "B": False,
        "C": True,
        "D": False
    }
    nested_expressions = [
        "(A and B) or C",
        "not (A or D)",
        "A and (B or not C)",
        "C and not A"
    ]
    output = evaluate_nested_logic(boolean_inputs, nested_expressions)
    print(output)