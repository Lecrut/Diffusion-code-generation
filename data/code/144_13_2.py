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
    results1 = evaluate_expression(input_assignments, expression1)
    results2 = evaluate_expression(input_assignments, expression2)
    results3 = evaluate_expression(input_assignments, expression3)
    results4 = evaluate_expression(input_assignments, expression4)
    print(f"Assignments: {input_assignments}")
    print(f"Expression '{expression1}': {results1}")
    print(f"Expression '{expression2}': {results2}")
    print(f"Expression '{expression3}': {results3}")
    print(f"Expression '{expression4}': {results4}")