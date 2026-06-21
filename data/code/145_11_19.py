def evaluate_nested_logic(inputs, expressions):
    results = {}
    for expr in expressions:
        try:
            result = eval(expr, {"__builtins__": None}, inputs)
            results[expr] = bool(result)
        except Exception:
            results[expr] = False
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
        "not A",
        "B or D"
    ]
    print(evaluate_nested_logic(boolean_inputs, nested_expressions))