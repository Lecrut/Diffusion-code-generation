import functools
def check_equivalence(expr1, expr2):
    if isinstance(expr1, bool) and isinstance(expr2, bool):
        return expr1 == expr2
    if isinstance(expr1, list) and isinstance(expr2, list):
        if len(expr1) != len(expr2):
            return False
        for b1, b2 in zip(expr1, expr2):
            if b1 != b2:
                return False
        return True
    return False
if __name__ == '__main__':
    print(f"Test 1 (True vs True): {check_equivalence(True, True)}")
    print(f"Test 2 (True vs False): {check_equivalence(True, False)}")
    expr_a = [True, False, True]
    expr_b = [True, False, True]
    print(f"Test 3 (List A vs List A): {check_equivalence(expr_a, expr_b)}")
    expr_c = [True, False, True]
    expr_d = [False, False, True]
    print(f"Test 4 (List A vs List D): {check_equivalence(expr_c, expr_d)}")
    expr_e = [True, True]
    expr_f = [True, False]
    print(f"Test 5 (List E vs List F): {check_equivalence(expr_e, expr_f)}")
    expr_g = [True, False]
    expr_h = [True, False]
    print(f"Test 6 (List G vs List H): {check_equivalence(expr_g, expr_h)}")
    expr_i = [True, False, True, False]
    expr_j = [True, False, True, False]
    print(f"Test 7 (Longer List Match): {check_equivalence(expr_i, expr_j)}")
    expr_k = [True, False]
    expr_l = [True, False, True]
    print(f"Test 8 (Different Lengths): {check_equivalence(expr_k, expr_l)}")