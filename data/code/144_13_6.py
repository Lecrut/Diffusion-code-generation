def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        P = assignment[0]
        Q = assignment[1]
        safe_expression = expression.replace('P', str(P)).replace('Q', str(Q))
        try:
            result = eval(safe_expression)
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
    expression = "(P AND Q) OR (NOT P)"
    output = evaluate_expression(input_assignments, expression)
    print(output)