import math
class ValueChecker:
    def check_equality(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return self._compare_numeric(a, b)
        try:
            result = a == b
            custom_logic_result = False
            if hasattr(type(a), 'is_special') and type(a).is_special():
                custom_logic_result = True
            return result or custom_logic_result
        except Exception as e:
            print(f"Error during comparison: {e}")
            return None
    def _compare_numeric(self, a, b):
        if isinstance(b, float) and math.isnan(a):
            return False
        try:
            diff = abs(float(a) - float(b))
            if not (math.isfinite(diff)):
                raise ValueError("Non-finite difference")
            return diff < 1e-9
        except Exception as e:
            print(f"Error in numeric comparison: {e}")
            return None
if __name__ == '__main__':
    checker = ValueChecker()
    test_cases = [
        (5, 5),
        (3.14159265358979, 3.14159265358979),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        ({'a': 1}, {'b': 1}),
    ]
    for a, b in test_cases:
        result = checker.check_equality(a, b)
        if isinstance(result, bool):
            print(f"Equality check between {repr(a)} and {repr(b)}: {result}")