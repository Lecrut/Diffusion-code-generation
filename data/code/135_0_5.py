def check_logical_equivalence(code1: str, code2: str) -> bool:
    try:
        exec(code1)
        exec(code2)
        return eval(f"code1 == code2")
    except Exception:
        return False
if __name__ == '__main__':
    code_a = "if x > 5: print('A')"
    code_b = "if x > 5: print('A')"
    print(f"A vs B: {check_logical_equivalence(code_a, code_b)}")
    code_c = "if x > 5: print('A')"
    code_d = "if x >= 6: print('A')"
    print(f"C vs D: {check_logical_equivalence(code_c, code_d)}")
    code_e = "if (x > 5 and y < 10): print('E')"
    code_f = "if y < 10 and x > 5: print('F')"
    print(f"E vs F: {check_logical_equivalence(code_e, code_f)}")
    code_g = "if x > 5: if y > 10: print('G')"
    code_h = "if y > 10: if x > 5: print('H')"
    print(f"G vs H: {check_logical_equivalence(code_g, code_h)}")
    code_i = "if not (x == 1): print('I')"
    code_j = "if x != 1: print('J')"
    print(f"I vs J: {check_logical_equivalence(code_i, code_j)}")