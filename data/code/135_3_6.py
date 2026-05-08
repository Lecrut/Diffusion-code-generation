def are_equivalent(expr1, expr2):
    def evaluate(expr):
        return eval(expr)
    try:
        val1 = evaluate(expr1)
        val2 = evaluate(expr2)
        return val1 == val2
    except Exception:
        return False
if __name__ == '__main__':
    expr_a = "True"
    expr_b = "True"
    print(are_equivalent(expr_a, expr_b))
    expr_c = "True"
    expr_d = "False"
    print(are_equivalent(expr_c, expr_d))
    expr_e = "(True or False)"
    expr_f = "True"
    print(are_equivalent(expr_e, expr_f))
    expr_g = "(A or B)"
    expr_h = "A or B"
    print(are_equivalent(expr_g, expr_h))
    expr_i = "True and False"
    expr_j = "False"
    print(are_equivalent(expr_i, expr_j))
    expr_k = "1"
    expr_l = "True"
    print(are_equivalent(expr_k, expr_l))