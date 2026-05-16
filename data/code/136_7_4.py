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
        return sympy.simplify(expr1_subs) == sympy.simplify(expr2_subs)
    except Exception:
        return False
def check_equivalence(expr1_str, expr2_str, variables):
    if not variables:
        return False
    result = evaluate_and_compare(expr1_str, expr2_str, variables)
    return result
if __name__ == '__main__':
    expr1_str_1 = "P"
    expr2_str_1 = "P"
    variables_1 = ["P"]
    result_1 = check_equivalence(expr1_str_1, expr2_str_1, variables_1)
    print(f"Test 1 (P == P): {result_1}")
    expr1_str_2 = "P"
    expr2_str_2 = "Q"
    variables_2 = ["P", "Q"]
    result_2 = check_equivalence(expr1_str_2, expr2_str_2, variables_2)
    print(f"Test 2 (P == Q): {result_2}")
    expr1_str_3 = "(P & Q)"
    expr2_str_3 = "(Q & P)"
    variables_3 = ["P", "Q"]
    result_3 = check_equivalence(expr1_str_3, expr2_str_3, variables_3)
    print(f"Test 3 ((P & Q) == (Q & P)): {result_3}")
    expr1_str_4 = "P"
    expr2_str_4 = "NOT P"
    variables_4 = ["P"]
    result_4 = check_equivalence(expr1_str_4, expr2_str_4, variables_4)
    print(f"Test 4 (P == NOT P): {result_4}")
    expr1_str_5 = "!(P & Q)"
    expr2_str_5 = "(!P | !Q)"
    variables_5 = ["P", "Q"]
    result_5 = check_equivalence(expr1_str_5, expr2_str_5, variables_5)
    print(f"Test 5 (!(P & Q) == (!P | !Q)): {result_5}")
    expr1_str_6 = "(P & Q)"
    expr2_str_6 = "(P | Q)"
    variables_6 = ["P", "Q"]
    result_6 = check_equivalence(expr1_str_6, expr2_str_6, variables_6)
    print(f"Test 6 ((P & Q) == (P | Q)): {result_6}")