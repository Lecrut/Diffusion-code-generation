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
        expr1_sub = expr1.subs(variables, {var: 1 for var in variables})
        expr2_sub = expr2.subs(variables, {var: 1 for var in variables})
        return sympy.simplify(expr1_sub) == sympy.simplify(expr2_sub)
    except Exception:
        return False
def check_equivalence(expr1_str, expr2_str, variables):
    if not variables:
        return False
    context = {var: True for var in variables}
    try:
        expr1 = sympy.sympify(expr1_str)
        expr2 = sympy.sympify(expr2_str)
        expr1_eval = expr1.subs(variables, context)
        expr2_eval = expr2.subs(variables, context)
        return sympy.simplify(expr1_eval) == sympy.simplify(expr2_eval)
    except Exception:
        return False
if __name__ == '__main__':
    expr_a = "(p AND q) OR (NOT p)"
    expr_b = "q OR (NOT p)"
    vars_1 = ['p', 'q']
    expr_c = "p OR q"
    expr_d = "(p OR q)"
    vars_2 = ['p', 'q']
    expr_e = "p AND (q OR r)"
    expr_f = "(p AND q) OR r"
    vars_3 = ['p', 'q', 'r']
    print(f"Expression A: {expr_a}")
    print(f"Expression B: {expr_b}")
    result_1 = check_equivalence(expr_a, expr_b, vars_1)
    print(f"Equivalence (A vs B): {result_1}\n")
    print(f"Expression C: {expr_c}")
    print(f"Expression D: {expr_d}")
    result_2 = check_equivalence(expr_c, expr_d, vars_2)
    print(f"Equivalence (C vs D): {result_2}\n")
    print(f"Expression E: {expr_e}")
    print(f"Expression F: {expr_f}")
    result_3 = check_equivalence(expr_e, expr_f, vars_3)
    print(f"Equivalence (E vs F): {result_3}\n")