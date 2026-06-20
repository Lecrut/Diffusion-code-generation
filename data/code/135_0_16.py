def normalize_string(s: str) -> str:
    return s.strip().lower()

def check_logical_equivalence(code1: str, code2: str) -> bool:
    normalized_code1 = normalize_string(code1)
    normalized_code2 = normalize_string(code2)
    return normalized_code1 == normalized_code2

if __name__ == '__main__':
    sample_a = " if x > 5 : print('A')"
    sample_b = "if x > 5: print('A')"
    print(f"A vs B: {check_logical_equivalence(sample_a, sample_b)}")
    
    sample_c = "if x > 5: print('B')"
    sample_d = "if x > 5: print('A')"
    print(f"C vs D: {check_logical_equivalence(sample_c, sample_d)}")
    
    sample_e = "if (x > 5 and y < 10): print('E')"
    sample_f = "if y < 10 and x > 5: print('F')"
    print(f"E vs F: {check_logical_equivalence(sample_e, sample_f)}")