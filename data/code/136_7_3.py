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
        subs1 = {var: sympy.Symbol(var) for var in variables}
        subs1.update({sympy.Symbol(var): sympy.Symbol(var) for var in variables})
        return expr1.equals(expr2)
    except Exception:
        return False
if __name__ == '__main__':
    expr1_str = "(A AND B) OR C"
    expr2_str = "A OR (B OR C)"
    variables = ['A', 'B', 'C']
    result = check_equivalence(expr1_str, expr2_str, variables)
    print(f"Expression 1: {expr1_str}")
    print(f"Expression 2: {expr2_str}")
    print(f"Logical Equivalence: {result}")
    print("-" * 20)
    expr3_str = "A AND (B OR C)"
    expr4_str = "(A AND B) OR C"
    result2 = check_equivalence(expr3_str, expr4_str, variables)
    print(f"Expression 3: {expr3_str}")
    print(f"Expression 4: {expr4_str}")
    print(f"Logical Equivalence: {result2}")
    print("-" * 20)
    expr5_str = "A"
    expr6_str = "A"
    result3 = check_equivalence(expr5_str, expr6_str, variables)
    print(f"Expression 5: {expr5_str}")
    print(f"Expression 6: {expr6_str}")
    print(f"Logical Equivalence: {result3}")