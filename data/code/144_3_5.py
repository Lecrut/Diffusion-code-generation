def evaluate_expression(input_combinations, expression_map):
    results = []
    for combo in input_combinations:
        current_result = None
        for rule_name, rule_func in expression_map.items():
            try:
                result = rule_func(combo)
                if current_result is None:
                    current_result = result
                else:
                    current_result = current_result and result
            except Exception:
                current_result = False
        results.append(current_result)
    return results
def and_expression(a, b):
    return a and b
def or_expression(a, b):
    return a or b
def not_expression(a):
    return not a
if __name__ == '__main__':
    input_data = [
        (False, True),
        (True, False),
        (False, False),
        (True, True)
    ]
    expression_rules = {
        "and": and_expression,
        "or": or_expression,
        "not": not_expression
    }
    output = evaluate_expression(input_data, expression_rules)
    print(output)