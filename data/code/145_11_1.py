def evaluate_nested_logic(inputs, expressions):
    results = {}
    for expr in expressions:
        try:
            result = eval(expr, {"__builtins__": None}, inputs)
            results[expr] = bool(result)
        except Exception:
            results[expr] = None
    return results
if __name__ == '__main__':
    boolean_inputs = {
        "A": True,
        "B": False,
        "C": True
    }
    nested_expressions = [
        "(A and B) or C",
        "not A",
        "(C or not B) and A",
        "A and (B or C)"
    ]
    calculated_results = evaluate_nested_logic(boolean_inputs, nested_expressions)
    print(calculated_results)