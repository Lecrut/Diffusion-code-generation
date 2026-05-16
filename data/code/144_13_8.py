def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        if len(assignment) != 2:
            raise ValueError("Each assignment must be a tuple of two truth values (P, Q).")
        p, q = assignment
        try:
            substitutions = {
                'P': p,
                'Q': q
            }
            evaluated_expression = expression.replace('P', str(p)).replace('Q', str(q))
            evaluated_expression = evaluated_expression.replace('&&', 'and').replace('||', 'or').replace('!', 'not')
            result = eval(evaluated_expression)
            results.append(result)
        except Exception as e:
            results.append(None) 
    return results
if __name__ == '__main__':
    input_assignments = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    expression_1 = "(P AND Q)"
    expression_2 = "(P OR NOT Q)"
    expression_3 = "(P AND (Q OR P))"
    results_1 = evaluate_expression(input_assignments, expression_1)
    results_2 = evaluate_expression(input_assignments, expression_2)
    results_3 = evaluate_expression(input_assignments, expression_3)
    print(f"Assignments: {input_assignments}")
    print(f"Expression 1: '{expression_1}'")
    print(f"Results 1: {results_1}")
    print("-" * 20)
    print(f"Expression 2: '{expression_2}'")
    print(f"Results 2: {results_2}")
    print("-" * 20)
    print(f"Expression 3: '{expression_3}'")
    print(f"Results 3: {results_3}")