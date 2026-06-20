def normalize_string(s: str) -> str:
    return s.strip().lower()

def check_logical_equivalence(str1: str, str2: str) -> bool:
    normalized_str1 = normalize_string(str1)
    normalized_str2 = normalize_string(str2)
    return normalized_str1 == normalized_str2

if __name__ == '__main__':
    sample_a = "  if x > 5: print('A')\n"
    sample_b = "if x > 5: print('A')"
    print(f"A vs B: {check_logical_equivalence(sample_a, sample_b)}")
    
    sample_c = "if x < 5: print('B')"
    sample_d = "if x <= 4: print('B')"
    print(f"C vs D: {check_logical_equivalence(sample_c, sample_d)}")
    
    sample_e = "if (x > 5 and y < 10): print('E')"
    sample_f = "if y < 10 and x > 5: print('F')"
    print(f"E vs F: {check_logical_equivalence(sample_e, sample_f)}")