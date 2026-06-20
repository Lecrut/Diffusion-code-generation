class StringComparer:
    @staticmethod
    def normalize_string(s: str) -> str:
        return s.strip().lower()

    @staticmethod
    def are_logically_equivalent(code1: str, code2: str) -> bool:
        normalized_code1 = StringComparer.normalize_string(code1)
        normalized_code2 = StringComparer.normalize_string(code2)
        return normalized_code1 == normalized_code2

if __name__ == '__main__':
    comparer = StringComparer()
    sample_a = "if x > 5: print('A')"
    sample_b = "if x > 5: print('A')"
    result_ab = comparer.are_logically_equivalent(sample_a, sample_b)
    print(f"A vs B: {result_ab}")

    sample_c = "if x > 5: print('A')"
    sample_d = "if x >= 6: print('A')"
    result_cd = comparer.are_logically_equivalent(sample_c, sample_d)
    print(f"C vs D: {result_cd}")

    sample_e = "if (x > 5 and y < 10): print('E')"
    sample_f = "if y < 10 and x > 5: print('F')"
    result_ef = comparer.are_logically_equivalent(sample_e, sample_f)
    print(f"E vs F: {result_ef}")