def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        P = assignment[0]
        Q = assignment[1]
        try:
            temp_expression = expression.replace('P', str(P)).replace('Q', str(Q))
            result = eval(temp_expression)
            results.append(result)
        except Exception:
            results.append(None)
    return results
if __name__ == '__main__':
    input_assignments = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    expression1 = "(P AND Q)"
    expression2 = "(P OR NOT Q)"
    expression3 = "(P AND (Q OR P))"
    results1 = evaluate_expression(input_assignments, expression1)
    results2 = evaluate_expression(input_assignments, expression2)
    results3 = evaluate_expression(input_assignments, expression3)
    print(f"Assignments: {input_assignments}")
    print("-" * 30)
    print(f"Expression: {expression1} results: {results1}")
    print(f"Expression: {expression2} results: {results2}")
    print(f"Expression: {expression3} results: {results3}")