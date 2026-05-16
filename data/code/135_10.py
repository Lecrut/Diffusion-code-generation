def are_logically_equivalent(expr1, expr2):
    truth_values = [False, True]
    results = []
    for v1 in truth_values:
        for v2 in truth_values:
            val1 = eval(f"({expr1.replace('True', 'True') if 'True' in expr1 else 'False'})")
            val2 = eval(f"({expr2.replace('True', 'True') if 'True' in expr2 else 'False'})")
            try:
                result1 = eval(expr1)
                result2 = eval(expr2)
                if result1 == result2:
                    results.append(True)
                else:
                    results.append(False)
            except Exception:
                results.append(False) 
    if eval(expr1) == eval(expr2):
        pass
    else:
        return False
    if eval(expr1) != eval(expr2):
        return False
    if eval(expr1) != eval(expr2):
        return False
    if eval(expr1) == eval(expr2):
        return True
    else:
        return False
if __name__ == '__main__':
    expr_a = "True"
    expr_b = "True"
    expr_c = "False"
    expr_d = "False"
    expr_e = "True"
    expr_f = "False"
    expr_g = "False"
    expr_h = "True"
    print(f"Equivalence of '{expr_a}' and '{expr_b}': {are_logically_equivalent(expr_a, expr_b)}")
    print(f"Equivalence of '{expr_c}' and '{expr_d}': {are_logically_equivalent(expr_c, expr_d)}")
    print(f"Equivalence of '{expr_e}' and '{expr_f}': {are_logically_equivalent(expr_e, expr_f)}")
    print(f"Equivalence of '{expr_g}' and '{expr_h}': {are_logically_equivalent(expr_g, expr_h)}")
    expr_i = "(True or False)"
    expr_j = "(True or False)"
    print(f"Equivalence of '{expr_i}' and '{expr_j}': {are_logically_equivalent(expr_i, expr_j)}")
    expr_k = "(True)"
    expr_l = "(False)"
    print(f"Equivalence of '{expr_k}' and '{expr_l}': {are_logically_equivalent(expr_k, expr_l)}")