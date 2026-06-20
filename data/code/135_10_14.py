def evaluate_expression(expr, variables):
    return eval(expr, {"__builtins__": None}, variables)

def are_logically_equivalent(expr1, expr2):
    if not isinstance(expr1, str) or not isinstance(expr2, str):
        raise ValueError("Both expressions must be strings.")
    
    inputs = [(False, False), (False, True), (True, False), (True, True)]
    for a, b in inputs:
        variables = {"a": a, "b": b}
        result1 = evaluate_expression(expr1, variables)
        result2 = evaluate_expression(expr2, variables)
        if result1 != result2:
            return False
    return True

if __name__ == '__main__':
    expression1 = "a and b"
    expression2 = "not a or not b"
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression1, expression2)}")
    
    expression3 = "a == b"
    expression4 = "(a == b)"
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    print(f"Are they logically equivalent? {are_logically_equivalent(expression3, expression4)}")