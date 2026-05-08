def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        if len(assignment) != 2:
            continue
        p, q = assignment
        try:
            if expression == "P":
                results.append(p)
            elif expression == "Q":
                results.append(q)
            elif expression == "P < Q":
                results.append(p < q)
            elif expression == "P > Q":
                results.append(p > q)
            elif expression == "P == Q":
                results.append(p == q)
            elif expression == "P AND Q":
                results.append(p and q)
            elif expression == "P OR Q":
                results.append(p or q)
            elif expression == "NOT P":
                results.append(not p)
            else:
                pass
        except TypeError:
            pass
    return results
if __name__ == '__main__':
    input_assignments = [
        (True, True),
        (True, False),
        (False, True),
        (False, False)
    ]
    expression1 = "P"
    expression2 = "Q"
    expression3 = "P < Q"
    expression4 = "P AND Q"
    expression5 = "NOT P"
    results1 = evaluate_expression(input_assignments, expression1)
    results2 = evaluate_expression(input_assignments, expression2)
    results3 = evaluate_expression(input_assignments, expression3)
    results4 = evaluate_expression(input_assignments, expression4)
    results5 = evaluate_expression(input_assignments, expression5)
    print(f"Expression: {expression1}")
    print(f"Results: {results1}")
    print("-" * 20)
    print(f"Expression: {expression2}")
    print(f"Results: {results2}")
    print("-" * 20)
    print(f"Expression: {expression3}")
    print(f"Results: {results3}")
    print("-" * 20)
    print(f"Expression: {expression4}")
    print(f"Results: {results4}")
    print("-" * 20)
    print(f"Expression: {expression5}")
    print(f"Results: {results5}")