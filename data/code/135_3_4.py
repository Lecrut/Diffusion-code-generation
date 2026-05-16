def are_equivalent(expr1, expr2):
    def evaluate(expr):
        return eval(expr)
    try:
        val1 = eval(expr1)
        val2 = eval(expr2)
        return val1 == val2
    except Exception:
        return False
if __name__ == '__main__':
    expr_a = "True"
    expr_b = "1"
    print(f"'{expr_a}' and '{expr_b}' are equivalent: {are_equivalent(expr_a, expr_b)}")
    expr_c = "(True or False)"
    expr_d = "True"
    print(f"'{expr_c}' and '{expr_d}' are equivalent: {are_equivalent(expr_c, expr_d)}")
    expr_e = "(not True) or False"
    expr_f = "False"
    print(f"'{expr_e}' and '{expr_f}' are equivalent: {are_equivalent(expr_e, expr_f)}")
    expr_g = "True and True"
    expr_h = "True"
    print(f"'{expr_g}' and '{expr_h}' are equivalent: {are_equivalent(expr_g, expr_h)}")
    expr_i = "False"
    expr_j = "0"
    print(f"'{expr_i}' and '{expr_j}' are equivalent: {are_equivalent(expr_i, expr_j)}")