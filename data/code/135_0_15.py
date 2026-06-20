def normalize_string(s: str) -> str:
    return s.strip().lower()

def check_logical_equivalence(code1: str, code2: str) -> bool:
    normalized_code1 = normalize_string(code1)
    normalized_code2 = normalize_string(code2)
    return normalized_code1 == normalized_code2

if __name__ == '__main__':
    code_a = " if x > 5: print('A') "
    code_b = "if x > 5: print('A')"
    print(f"A vs B: {check_logical_equivalence(code_a, code_b)}")
    code_c = "if x > 5: print('B')"
    code_d = "if x > 5: print('A')"
    print(f"C vs D: {check_logical_equivalence(code_c, code_d)}")