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
    print(f"'{expr_a}' vs '{expr_b}': {are_equivalent(expr_a, expr_b)}")
    expr_c = "(True or False)"
    expr_d = "True"
    print(f"'{expr_c}' vs '{expr_d}': {are_equivalent(expr_c, expr_d)}")
    expr_e = "(False and True)"
    expr_f = "False"
    print(f"'{expr_e}' vs '{expr_f}': {are_equivalent(expr_e, expr_f)}")
    expr_g = "True"
    expr_h = "True or True"
    print(f"'{expr_g}' vs '{expr_h}': {are_equivalent(expr_g, expr_h)}")
    expr_i = "False"
    expr_j = "0"
    print(f"'{expr_i}' vs '{expr_j}': {are_equivalent(expr_i, expr_j)}")