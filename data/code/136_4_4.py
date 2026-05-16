def evaluate_boolean_expression(expression, variables):
    result = expression
    for var_name, value in variables.items():
        result = result.replace(var_name, str(value))
    return eval(result)
if __name__ == '__main__':
    expression1 = "(A and B) or (not C)"
    variables1 = {"A": True, "B": False, "C": True}
    result1 = evaluate_boolean_expression(expression1, variables1)
    print(f"Expression: {expression1}, Variables: {variables1}, Result: {result1}")
    expression2 = "not (X or Y)"
    variables2 = {"X": True, "Y": False}
    result2 = evaluate_boolean_expression(expression2, variables2)
    print(f"Expression: {expression2}, Variables: {variables2}, Result: {result2}")
    expression3 = "A and (B or C)"
    variables3 = {"A": True, "B": True, "C": False}
    result3 = evaluate_boolean_expression(expression3, variables3)
    print(f"Expression: {expression3}, Variables: {variables3}, Result: {result3}")