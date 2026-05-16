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
    code_c = "if x > 5: print('B')"
    code_d = "if x > 5: print('A')"
    code_e = "if x > 5: print('C')"
    code_f = "if x > 5: print('A')"
    print(f"A vs B: {check_logical_equivalence(code_a, code_b)}")
    print(f"A vs C: {check_logical_equivalence(code_a, code_c)}")
    print(f"A vs D: {check_logical_equivalence(code_a, code_d)}")
    print(f"A vs E: {check_logical_equivalence(code_a, code_e)}")
    print(f"A vs F: {check_logical_equivalence(code_a, code_f)}")
    code_g = "if (x > 5 and y < 10): print('G')"
    code_h = "if x > 5 and y < 10: print('G')"
    code_i = "if x > 5 or y < 10: print('H')"
    print(f"G vs H: {check_logical_equivalence(code_g, code_h)}")
    print(f"G vs I: {check_logical_equivalence(code_g, code_i)}")