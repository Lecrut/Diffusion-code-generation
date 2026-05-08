def evaluate_expression(input_combinations, expression_map):
    results = []
    for combo in input_combinations:
        current_result = None
        for expression_str in expression_map:
            if expression_str == "AND":
                if all(combo):
                    current_result = True
                else:
                    current_result = False
            elif expression_str == "OR":
                if any(combo):
                    current_result = True
                else:
                    current_result = False
            elif expression_str == "NOT":
                if len(combo) == 1:
                    current_result = not combo[0]
                else:
                    current_result = False
            else:
                continue
        results.append(current_result)
    return results
if __name__ == '__main__':
    input_data = [
        (False, False),
        (False, True),
        (True, False),
        (True, True)
    ]
    expression_definitions = [
        "AND",
        "OR",
        "NOT"
    ]
    output = evaluate_expression(input_data, expression_definitions)
    print(output)