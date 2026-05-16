def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        P = assignment[0]
        Q = assignment[1]
        try:
            scope = {'P': P, 'Q': Q}
            result = eval(expression, {}, scope)
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
    expression_to_evaluate = "(P AND Q) OR (NOT P)"
    output = evaluate_expression(input_assignments, expression_to_evaluate)
    print(output)