def evaluate_expression(assignments, expression):
    results = []
    for assignment in assignments:
        if len(assignment) != 2:
            raise ValueError("Each assignment must be a tuple of two truth values (P, Q).")
        P, Q = assignment
        try:
            subst_expression = expression.replace('P', str(P)).replace('Q', str(Q))
            result = eval(subst_expression)
            results.append(result)
        except Exception as e:
            results.append(f"Error evaluating: {e}")
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
    print(f"Expression: {expression_1}")
    output_1 = evaluate_expression(input_assignments, expression_1)
    print(f"Results: {output_1}\n")
    print(f"Expression: {expression_2}")
    output_2 = evaluate_expression(input_assignments, expression_2)
    print(f"Results: {output_2}\n")
    print(f"Expression: {expression_3}")
    output_3 = evaluate_expression(input_assignments, expression_3)
    print(f"Results: {output_3}\n")