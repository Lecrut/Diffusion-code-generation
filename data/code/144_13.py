def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        if not assignment:
            results.append(False)
            continue
        if expression == "P":
            results.append(assignment[0])
        elif expression == "Q":
            results.append(assignment[1])
        elif expression == "P == Q":
            results.append(assignment[0] == assignment[1])
        elif expression == "P and Q":
            results.append(assignment[0] and assignment[1])
        elif expression == "P or Q":
            results.append(assignment[0] or assignment[1])
        elif expression == "not P":
            results.append(not assignment[0])
        elif expression == "not Q":
            results.append(not assignment[1])
        elif expression == "P == True":
            results.append(assignment[0] == True)
        elif expression == "Q == False":
            results.append(assignment[1] == False)
        else:
            raise ValueError(f"Unsupported expression: {expression}")
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
    expression3 = "P == Q"
    expression4 = "P and Q"
    expression5 = "P or Q"
    expression6 = "not P"
    expression7 = "P == True"
    expression8 = "Q == False"
    print(f"Assignments: {input_assignments}")
    results1 = evaluate_expression(input_assignments, expression1)
    print(f"Expression: {expression1}, Results: {results1}")
    results2 = evaluate_expression(input_assignments, expression2)
    print(f"Expression: {expression2}, Results: {results2}")
    results3 = evaluate_expression(input_assignments, expression3)
    print(f"Expression: {expression3}, Results: {results3}")
    results4 = evaluate_expression(input_assignments, expression4)
    print(f"Expression: {expression4}, Results: {results4}")
    results5 = evaluate_expression(input_assignments, expression5)
    print(f"Expression: {expression5}, Results: {results5}")
    results6 = evaluate_expression(input_assignments, expression6)
    print(f"Expression: {expression6}, Results: {results6}")
    results7 = evaluate_expression(input_assignments, expression7)
    print(f"Expression: {expression7}, Results: {results7}")
    results8 = evaluate_expression(input_assignments, expression8)
    print(f"Expression: {expression8}, Results: {results8}")