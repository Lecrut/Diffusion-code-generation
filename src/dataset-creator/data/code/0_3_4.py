import json
class ValueChecker:
    def compare(self, a, b):
        if isinstance(a, dict) and isinstance(b, dict):
            return self._compare_dicts(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            return self._compare_lists(a, b)
        else:
            try:
                return a == b
            except TypeError:
                raise ValueError("Unsupported types for comparison")
    def _compare_dicts(self, d1, d2):
        if set(d1.keys()) != set(d2.keys()):
            return False
        for key in d1:
            if not self.compare(d1[key], d2[key]):
                return False
        return True
    def _compare_lists(self, l1, l2):
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if not self.compare(l1[i], l2[i]):
                return False
        return True
if __name__ == '__main__':
    checker = ValueChecker()
    test_cases = [
        ({"a": 1, "b": {"x": 2}}, {"a": 1, "b": {"x": 2}}),
        ([1, 2, 3], [4, 5, 6]),
        ("string", "different"),
        (None, None),
    ]
    for i in range(len(test_cases)):
        a = test_cases[i][0]
        b = test_cases[i][1]
        result = checker.compare(a, b)
        print(f"Test {i + 1}: Expected {result}, Got {a} vs {b}")