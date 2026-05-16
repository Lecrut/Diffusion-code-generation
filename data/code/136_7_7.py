import sympy
def simplify_expression(expression_str):
    try:
        expr = sympy.sympify(expression_str)
        return sympy.simplify(expr)
    except sympy.SympifyError:
        return None
def evaluate_and_compare(expr1_str, expr2_str, variables):
    try:
        expr1 = sympy.sympify(expr1_str)
        expr2 = sympy.sympify(expr2_str)
        subs1 = {var: float(val) for var, val in variables.items()}
        subs2 = {var: float(val) for var, val in variables.items()}
        val1 = expr1.subs(subs1).evalf()
        val2 = expr2.subs(subs2).evalf()
        return abs(val1 - val2) < 1e-9
    except Exception:
        return False
def find_variables(expression_str):
    import re
    variables = set()
    for match in re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', expression_str):
        variables.add(match)
    return sorted(list(variables))
if __name__ == '__main__':
    expression1 = "A + B"
    expression2 = "(A + B)"
    variables = {'A': 2, 'B': 3}
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Variables: {variables}")
    is_equivalent = evaluate_and_compare(expression1, expression2, variables)
    print(f"Are the expressions logically equivalent for these values? {is_equivalent}")
    expression3 = "A * (B + C)"
    expression4 = "(A * B) + (A * C)"
    variables_3 = {'A': 1, 'B': 2, 'C': 4}
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    print(f"Variables: {variables_3}")
    is_equivalent_2 = evaluate_and_compare(expression3, expression4, variables_3)
    print(f"Are the expressions logically equivalent for these values? {is_equivalent_2}")