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
def sample_expression_1(a, b, c):
    return (a and b) or c
def sample_expression_2(a, b):
    return a or b
def sample_expression_3(a, b, c):
    return a and b and c
if __name__ == '__main__':
    input_data = [
        (True, False, True),
        (True, True, True),
        (False, False, False),
        (True, True, False)
    ]
    expression_map = {
        "expr1": sample_expression_1,
        "expr2": sample_expression_2,
        "expr3": sample_expression_3
    }
    output = evaluate_expression(input_data, expression_map)
    print(output)