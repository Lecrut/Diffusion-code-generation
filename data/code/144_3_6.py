def evaluate_expression(input_combinations, expression_rules):
    results = []
    for combo in input_combinations:
        current_result = None
        for rule in expression_rules:
            if rule[0] == 'AND':
                if all(combo[i] for i in range(len(combo))):
                    current_result = True
            elif rule[0] == 'OR':
                if any(combo[i] for i in range(len(combo))):
                    current_result = True
            elif rule[0] == 'NOT':
                if len(combo) == 1:
                    current_result = not combo[0]
                else:
                    current_result = False
            else:
                current_result = False
        results.append(current_result)
    return results
if __name__ == '__main__':
    input_data = [
        (False, False),
        (False, True),
        (True, False),
        (True, True)
    ]
    expression_rules = [
        ('AND', [0, 1]),
        ('OR', [0, 1]),
        ('NOT', [0]),
        ('NOT', [1])
    ]
    output = evaluate_expression(input_data, expression_rules)
    print(output)