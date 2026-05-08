def evaluate_boolean_expression(expression, variables):
    result = expression
    for var_name, value in variables.items():
        result = result.replace(var_name, str(value))
    return eval(result)
if __name__ == '__main__':
    expression_string = "A and (B or not C)"
    variable_values = {
        "A": True,
        "B": False,
        "C": True
    }
    final_result = evaluate_boolean_expression(expression_string, variable_values)
    print(final_result)