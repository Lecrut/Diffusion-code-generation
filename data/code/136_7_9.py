import sympy
def simplify_expression(expression_str):
    try:
        expr = sympy.sympify(expression_str)
        return expr.simplify()
    except sympy.SympifyError:
        return None
def check_equivalence(expr1_str, expr2_str, variables):
    try:
        expr1 = sympy.sympify(expr1_str)
        expr2 = sympy.sympify(expr2_str)
        expr1_subs = expr1.subs(variables, {v: sympy.Symbol(v) for v in variables})
        expr2_subs = expr2.subs(variables, {v: sympy.Symbol(v) for v in variables})
        return expr1_subs == expr2_subs
    except Exception:
        return False
if __name__ == '__main__':
    expr1_str = "(A OR B) AND (NOT A OR C)"
    expr2_str = "(A OR C) AND (NOT A OR B)"
    variables = ['A', 'B', 'C']
    result = check_equivalence(expr1_str, expr2_str, variables)
    print(f"Expression 1: {expr1_str}")
    print(f"Expression 2: {expr2_str}")
    print(f"Logical Equivalence: {result}")