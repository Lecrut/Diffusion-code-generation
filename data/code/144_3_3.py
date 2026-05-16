def evaluate_expression(input_combinations, expression_map):
    results = []
    for combo in input_combinations:
        current_result = None
        for rule_name, rule_function in expression_map.items():
            try:
                result = rule_function(combo)
                if current_result is None:
                    current_result = result
                else:
                    current_result = current_result and result
            except Exception:
                current_result = False
        results.append(current_result)
    return results
def and_operation(a, b):
    return a and b
def or_operation(a, b):
    return a or b
def not_operation(a):
    return not a
if __name__ == '__main__':
    input_data = [
        (False, True),
        (True, False),
        (False, False),
        (True, True)
    ]
    expression_rules = {
        "A_and_B": lambda combo: combo[0] and combo[1],
        "A_or_B": lambda combo: combo[0] or combo[1],
        "not_A": lambda combo: not combo[0],
        "not_B": lambda combo: not combo[1]
    }
    output = evaluate_expression(input_data, expression_rules)
    print(output)