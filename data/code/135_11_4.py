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
    print(f"Test 3 (List equal): {check_equivalence(expr_a, expr_b)}")
    expr_c = [True, False, False]
    expr_d = [True, False, True]
    print(f"Test 4 (List unequal): {check_equivalence(expr_c, expr_d)}")
    expr_e = [True, True]
    expr_f = [True, True]
    print(f"Test 5 (List equal 2 elements): {check_equivalence(expr_e, expr_f)}")
    expr_g = [True, False]
    expr_h = [False, True]
    print(f"Test 6 (List different order): {check_equivalence(expr_g, expr_h)}")
    expr_i = [True]
    expr_j = [True, True]
    print(f"Test 7 (List different length): {check_equivalence(expr_i, expr_j)}")
    expr_k = [True, True, True]
    expr_l = [True, True]
    print(f"Test 8 (List different length): {check_equivalence(expr_k, expr_l)}")
    expr_m = [True, False]
    expr_n = [True, False]
    print(f"Test 9 (List equal 2 elements): {check_equivalence(expr_m, expr_n)}")