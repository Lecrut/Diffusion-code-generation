def evaluate_nested_logic(inputs, expressions):
    results = {}
    for expr in expressions:
        if expr in inputs:
            results[expr] = inputs[expr]
        else:
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
        "A",
        "B",
        "C",
        "D",
        "A and C",
        "B or D",
        "not A",
        "C and not B"
    ]
    calculated_results = evaluate_nested_logic(boolean_inputs, nested_expressions)
    print(calculated_results)