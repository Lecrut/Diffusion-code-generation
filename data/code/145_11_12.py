def validate_inputs(inputs):
    if not isinstance(inputs, dict) or not all(isinstance(k, str) and isinstance(v, bool) for k, v in inputs.items()):
        raise ValueError("Inputs must be a dictionary with string keys and boolean values.")

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
        "C": True,
        "D": False
    }
    validate_inputs(boolean_inputs)
    nested_expressions = [
        "(A and B) or C",
        "not A"
    ]
    results = evaluate_nested_logic(boolean_inputs, nested_expressions)
    print(results)