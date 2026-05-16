def evaluate_nested_logic(inputs, expressions):
    results = {}
    for expr in expressions:
        if expr in inputs:
            results[expr] = inputs[expr]
        else:
            results[expr] = False
    return results
if __name__ == '__main__':
    boolean_inputs = {
        "A": True,
        "B": False,
        "C": True
    }
    nested_expressions = [
        "A",
        "B",
        "C",
        "D",
        "A and B",
        "C or A",
        "not B"
    ]
    calculated_results = evaluate_nested_logic(boolean_inputs, nested_expressions)
    print(calculated_results)