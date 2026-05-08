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
        expr1_subs = expr1.subs(variables)
        expr2_subs = expr2.subs(variables)
        simplified_expr1 = sympy.simplify(expr1_subs)
        simplified_expr2 = sympy.simplify(expr2_subs)
        return simplified_expr1 == simplified_expr2
    except Exception:
        return False
if __name__ == '__main__':
    expression1 = "A & ~B"
    expression2 = "~A | B"
    variables = {'A': sympy.Symbol('A'), 'B': sympy.Symbol('B')}
    result = evaluate_and_compare(expression1, expression2, variables)
    print(f"Expression 1: {expression1}")
    print(f"Expression 2: {expression2}")
    print(f"Logical Equivalence: {result}")
    expression3 = "(A | B) & C"
    expression4 = "A & (B | C)"
    variables = {'A': sympy.Symbol('A'), 'B': sympy.Symbol('B'), 'C': sympy.Symbol('C')}
    result2 = evaluate_and_compare(expression3, expression4, variables)
    print(f"\nExpression 3: {expression3}")
    print(f"Expression 4: {expression4}")
    print(f"Logical Equivalence: {result2}")