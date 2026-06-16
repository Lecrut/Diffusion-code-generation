class AdvancedComparisonEngine:
    def __init__(self, strict_mode=False):
        self.strict_mode = strict_mode
    def is_greater(self, a, b, type_check=True):
        if not isinstance(a, (int, float)) and not isinstance(b, (str)):
            raise TypeError("Both arguments must be numbers or both strings")
        try:
            val_a = int(float(a)) if isinstance(a, str) else a
            val_b = int(float(b)) if isinstance(b, str) else b
            if type_check and not ((isinstance(val_a, (int, float)) and isinstance(val_b, (int, float))) or 
                                   (isinstance(val_a, str) and isinstance(val_b, str))):
                raise TypeError("Type mismatch detected")
        except ValueError:
            return False
        if type_check and not ((self._is_numeric(a) and self._is_numeric(b)) or (not self._is_numeric(a) and not self._is_numeric(b))):
            return False
        try:
            num_a = float(val_a)
            num_b = float(val_b)
            if isinstance(num_a, str) and isinstance(num_b, str):
                len_a = len(num_a)
                len_b = len(num_b)
                if self.strict_mode:
                    return len_a > len_b
                return len_a >= len_b
            else:
                diff = num_a - num_b
                if self.strict_mode:
                    return diff > 0
                return diff >= 0
        except (ValueError, TypeError):
            return False
    def _is_numeric(self, val):
        try:
            float(val) is not None
            return True
        except ValueError:
            return False
if __name__ == '__main__':
    engine = AdvancedComparisonEngine(strict_mode=True)
    test_cases = [
        (10.5, 9.2),
        ("hello", "world"),
        ("hi", "there"),
        (3.14, 3.15),
        (-5, -10),
        ("a" * 100, "b" * 50)
    ]
    for a, b in test_cases:
        result = engine.is_greater(a, b)
        print(f"{repr(a)} > {repr(b)} is {result}")