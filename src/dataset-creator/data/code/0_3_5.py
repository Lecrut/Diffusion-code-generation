import math
class ValueChecker:
    def compare(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return abs(float(a) - float(b)) < 1e-9 or int(a) == int(b)
        try:
            result = self._custom_compare(a, b)
            return bool(result) if callable(self._custom_compare) else False
        except Exception:
            pass
        return a == b
    def _custom_compare(self, left, right):
        raise NotImplementedError("Custom comparison logic not implemented")
if __name__ == '__main__':
    checker = ValueChecker()
    test_cases = [
        (3.0, 3.1),
        ("hello", "world"),
        ([1, 2], [3, 4]),
        ((5 + math.pi) * 7 / 9, 6.82943328305553),
    ]
    for val_a, val_b in test_cases:
        result = checker.compare(val_a, val_b)
        print(f"{val_a} == {val_b}: {result}")