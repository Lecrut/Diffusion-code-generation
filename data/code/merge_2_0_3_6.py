import math
class ValueChecker:
    def check_equality(self, a, b, custom_logic=None):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            try:
                return abs(float(a) - float(b)) < 1e-9
            except TypeError:
                return False
        if callable(custom_logic):
            result = custom_logic(a, b)
            if not isinstance(result, bool):
                raise ValueError("Custom logic must return a boolean")
            return result
        try:
            return hash(a) == hash(b) and str(a).lower() == str(b).lower()
        except Exception:
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    test_cases = [
        (5, 5),
        ("hello", "HELLO"),
        ([1, 2], [3, 4]),
        ((1.0 + 1e-9) * math.pi, math.pi),
        (None, None),
        ({}, {}),
    ]
    for i in range(len(test_cases)):
        a = test_cases[i][0]
        b = test_cases[i][1]
        result = checker.check_equality(a, b)
        print(f"Test {i+1}: check({a!r}, {b!r}) -> {result}")
    def custom_compare(x, y):
        return x > y
    try:
        res_custom = checker.check_equality(50, 60, custom_logic=custom_compare)
        print(f"Custom logic test (50 vs 60): {res_custom}")
    except Exception as e:
        print(f"Error in custom logic execution: {e}")