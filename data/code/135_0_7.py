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
    code_c = "if x == 10: print('C')"
    code_d = "if x > 5: print('D')"
    code_e = "if x > 5: print('A')"
    code_f = "if x > 5: print('E')"
    code_g = "if x > 5: print('A')"
    code_h = "if x > 5: print('F')"
    code_i = "if x == 10: print('F')"
    print(f"A and B equivalent: {check_logical_equivalence(code_a, code_b)}")
    print(f"A and D equivalent: {check_logical_equivalence(code_a, code_d)}")
    print(f"A and E equivalent: {check_logical_equivalence(code_a, code_e)}")
    print(f"A and G equivalent: {check_logical_equivalence(code_a, code_g)}")
    print(f"A and H equivalent: {check_logical_equivalence(code_a, code_h)}")
    print(f"A and I equivalent: {check_logical_equivalence(code_a, code_i)}")