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
def simple_and(a, b):
    return a and b
def simple_or(a, b):
    return a or b
def simple_not(a):
    return not a
if __name__ == '__main__':
    input_data = [
        (False, True),
        (True, False),
        (False, False),
        (True, True)
    ]
    expression_rules = {
        "and_op": simple_and,
        "or_op": simple_or,
        "not_op": simple_not
    }
    output = evaluate_expression(input_data, expression_rules)
    print(output)