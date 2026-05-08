import sympy
def simplify_expression(expression_str):
    try:
        expr = sympy.sympify(expression_str)
        return expr.simplify()
    except sympy.SympifyError:
        return None
def evaluate_and_compare(expr1_str, expr2_str, variables):
    try:
        expr1 = sympy.sympify(expr1_str)
        expr2 = sympy.sympify(expr2_str)
        expr1_sub = expr1.subs(variables, {v: 1 for v in variables})
        expr2_sub = expr2.subs(variables, {v: 1 for v in variables})
        return expr1.equals(expr2)
    except Exception:
        return False
def check_equivalence(expr1_str, expr2_str, variables):
    if expr1_str == expr2_str:
        return True
    try:
        expr1 = sympy.sympify(expr1_str)
        expr2 = sympy.sympify(expr2_str)
        all_vars = set()
        for s in [expr1_str, expr2_str]:
            for char in s:
                if 'a' <= char <= 'z':
                    all_vars.add(char)
        if not all_vars:
            return sympy.simplify(expr1) == sympy.simplify(expr2)
        var_list = sorted(list(all_vars))
        n = len(var_list)
        for i in range(2**n):
            assignment = {}
            temp_i = i
            for j in range(n):
                assignment[var_list[j]] = bool(temp_i & 1)
                temp_i >>= 1
            try:
                val1 = expr1.subs(assignment, {v: 1 if v in ('True', 'True') else 0 for v in var_list})
                val2 = expr2.subs(assignment, {v: 1 if v in ('True', 'True') else 0 for v in var_list})
                if val1 != val2:
                    return False
            except Exception:
                continue
        return True
    except Exception:
        return False
if __name__ == '__main__':
    expr1 = "a AND (b OR c)"
    expr2 = "(a AND b) OR c"
    variables = ['a', 'b', 'c']
    result = check_equivalence(expr1, expr2, variables)
    print(f"Expression 1: {expr1}")
    print(f"Expression 2: {expr2}")
    print(f"Variables: {variables}")
    print(f"Logical Equivalence: {result}")
    print("-" * 20)
    expr3 = "a OR (b AND c)"
    expr4 = "(a OR b) AND (a OR c)"
    result2 = check_equivalence(expr3, expr4, variables)
    print(f"Expression 3: {expr3}")
    print(f"Expression 4: {expr4}")
    print(f"Variables: {variables}")
    print(f"Logical Equivalence: {result2}")