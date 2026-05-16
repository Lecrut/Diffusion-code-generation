def are_equivalent(expr1, expr2):
    if expr1 == expr2:
        return True
    try:
        result1 = eval(f"({expr1})")
        result2 = eval(f"({expr2})")
        return result1 == result2
    except Exception:
        return False
if __name__ == '__main__':
    expr_a = "True or False"
    expr_b = "True"
    print(f"'{expr_a}' vs '{expr_b}': {are_equivalent(expr_a, expr_b)}")
    expr_c = "(A and B) or C"
    expr_d = "A and (B or C)"
    print(f"'{expr_c}' vs '{expr_d}': {are_equivalent(expr_c, expr_d)}")
    expr_e = "True"
    expr_f = "True or False"
    print(f"'{expr_e}' vs '{expr_f}': {are_equivalent(expr_e, expr_f)}")
    expr_g = "False"
    expr_h = "False"
    print(f"'{expr_g}' vs '{expr_h}': {are_equivalent(expr_g, expr_h)}")
    expr_i = "True"
    expr_j = "False"
    print(f"'{expr_i}' vs '{expr_j}': {are_equivalent(expr_i, expr_j)}")