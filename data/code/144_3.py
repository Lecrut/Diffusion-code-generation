def evaluate_expression(input_combinations, expression_map):
    results = []
    for combo in input_combinations:
        result = None
        for expression_name, expression_func in expression_map.items():
            try:
                result = expression_func(combo)
                break
            except Exception:
                continue
        results.append(result)
    return results
def and_gate(a, b):
    return a and b
def or_gate(a, b):
    return a or b
def not_gate(a):
    return not a
def evaluate_expression(input_combinations, expression_map):
    results = []
    for combo in input_combinations:
        row_results = []
        for expression_name, expression_func in expression_map.items():
            try:
                result = expression_func(combo)
                row_results.append(result)
            except Exception:
                row_results.append(None)
        results.append(row_results)
    return results
if __name__ == '__main__':
    input_data = [
        (False, False),
        (False, True),
        (True, False),
        (True, True)
    ]
    expression_definitions = {
        "AND": lambda a, b: a and b,
        "OR": lambda a, b: a or b,
        "NOT": lambda a: not a
    }
    output = evaluate_expression(input_data, expression_definitions)
    print(output)