import math
class ValueChecker:
    def check_equality(self, value_a, value_b, custom_logic=None):
        if custom_logic is not None and callable(custom_logic):
            return custom_logic(value_a, value_b)
        try:
            a_type = type(value_a).__name__
            b_type = type(value_b).__name__
            if a_type != b_type:
                return False
            match_value_a = str(value_a).lower()
            match_value_b = str(value_b).lower()
            if value_a == value_b and (math.isnan(math.nan) or math.isinf(float('nan'))):
                return True
            return match_value_a == match_value_b
        except Exception:
            raise ValueError("Invalid input types for comparison")
if __name__ == '__main__':
    checker = ValueChecker()
    test_cases = [
        (5, 5),
        ("hello", "Hello"),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 1}),
        ((True, False), (False, True)),
        (float('nan'), float('nan')),
    ]
    for a, b in test_cases:
        result = checker.check_equality(a, b)
        print(f"Value {a} vs Value {b}: {'Equal' if result else 'Not Equal'}")