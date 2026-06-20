def evaluate_expression(expr, variables):
    return eval(expr, {"__builtins__": None}, variables)

def generate_truth_table(variables):
    if not variables:
        yield {}
    else:
        var = variables[0]
        for rest in generate_truth_table(variables[1:]):
            yield {var: False, **rest}
            yield {var: True, **rest}

def are_logically_equivalent(expr1, expr2):
    variables = list(set(expr1) & set(expr2))
    if not all(var in {'True', 'False'} for var in variables):
        raise ValueError("Expressions contain non-boolean variables")
    
    truth_table = generate_truth_table(variables)
    for assignment in truth_table:
        result1 = evaluate_expression(expr1, assignment)
        result2 = evaluate_expression(expr2, assignment)
        if result1 != result2:
            return False
    return True

if __name__ == '__main__':
    expression1 = "a and b"
    expression2 = "b and a"
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression1, expression2)}")
    
    expression3 = "a == b"
    expression4 = "(a == b)"
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression3, expression4)}")