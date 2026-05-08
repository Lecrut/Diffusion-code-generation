def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        P = assignment[0]
        Q = assignment[1]
        try:
            result = eval(expression, {"__builtins__": None}, {"P": P, "Q": Q})
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
    expression_str = "(P AND Q) OR (NOT P AND Q)"
    output = evaluate_expression(input_assignments, expression_str)
    print(output)