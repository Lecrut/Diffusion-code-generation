def check_logical_equivalence(code1, code2):
    try:
        exec(code1)
        exec(code2)
        return True
    except Exception:
        return False
if __name__ == '__main__':
    code_a = "if x > 5: print('A')"
    code_b = "if x > 5: print('B')"
    code_c = "if x > 5: print('A')"
    code_d = "if x > 5: print('C')"
    code_e = "if x > 10: print('A')"
    print(f"A vs B: {check_logical_equivalence(code_a, code_b)}")
    print(f"A vs C: {check_logical_equivalence(code_a, code_c)}")
    print(f"A vs D: {check_logical_equivalence(code_a, code_d)}")
    print(f"A vs E: {check_logical_equivalence(code_a, code_e)}")