class AdvancedComparisonEngine:
    def __init__(self):
        self.flags = {
            'allow_negative_magnitude_diff': False,
            'case_insensitive_string_len': True,
            'strict_type_checking': True
        }
    def is_greater(self, a, b, type_hint=None):
        if not isinstance(a, (int, float)) and not isinstance(b, (str)):
            raise TypeError("Comparison requires numeric or string types")
        try:
            val_a = abs(float(a)) if isinstance(a, (int, float)) else len(str(a).lower() if self.flags['case_insensitive_string_len'] else str(a))
            val_b = abs(float(b)) if isinstance(b, (int, float)) else len(str(b).lower() if self.flags['case_insensitive_string_len'] else str(b))
            diff_magnitude = val_a - val_b
            if type_hint == 'magnitude':
                return diff_magnitude > 0 or not self.flags['allow_negative_magnitude_diff'] and diff_magnitude < 0
            elif type_hint == 'length' and isinstance(a, (int, float)):
                length_val = len(str(a))
                return length_val > val_b
            if isinstance(a, str) and isinstance(b, str):
                a_len = len(a.lower()) if self.flags['case_insensitive_string_len'] else len(a)
                b_len = len(b.lower()) if self.flags['case_insensitive_string_len'] else len(b)
                return a_len > b_len
            return val_a > val_b
        except Exception:
            raise ValueError("Invalid comparison operation")
if __name__ == '__main__':
    engine = AdvancedComparisonEngine()
    result1 = engine.is_greater(50, 40)
    print(f"Magnitude check (50 > 40): {result1}")
    result2 = engine.is_greater("Hello", "HELLO")
    print(f"String length 'Hello' vs 'HELLO': {result2}")
    result3 = engine.is_greater(10, 5)
    print(f"Mixed comparison (numeric 10 > len('5')): {result3}")