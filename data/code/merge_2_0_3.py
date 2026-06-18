import math
class ValueChecker:
    def check_equality(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return abs(float(a) - float(b)) < 1e-9 or int(math.isclose(a, b))
        try:
            result = self.custom_compare(a, b)
            return bool(result) if callable(self.custom_compare) else False
        except Exception:
            return a == b
    def custom_compare(self, x, y):
        raise NotImplementedError("Custom comparison logic must be implemented")
if __name__ == '__main__':
    checker = ValueChecker()
    test_cases = [
        (3.0, 3.1),
        ("hello", "world"),
        ([1, 2], [1, 2]),
        ({'a': 1}, {'b': 1}),
        ((None,), ()),
    ]
    for val_a, val_b in test_cases:
        result = checker.check_equality(val_a, val_b)
        print(f"{val_a} == {val_b}: {result}")