def evaluate_boolean_expression(expression, variables):
    for var_name, value in variables.items():
        expression = expression.replace(var_name, str(value))
    return eval(expression)

if __name__ == '__main__':
    expressions = {
        "(A and B) or not C": {"A": True, "B": False, "C": True},
        "not (X or Y)": {"X": True, "Y": False},
        "A and (B or C)": {"A": True, "B": True, "C": False}
    }
    
    for expr, vars in expressions.items():
        result = evaluate_boolean_expression(expr, vars)
        print(f"Expression: {expr}, Variables: {vars}, Result: {result}")