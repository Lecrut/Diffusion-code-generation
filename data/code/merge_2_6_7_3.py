class AdvancedComparisonEngine:
    def __init__(self):
        self.flags = {
            'strict_types': True,
            'allow_floats': False,
            'case_sensitive_strings': True
        }
    def is_greater(self, a, b, flag_override=None):
        if flag_override:
            for key in ['strict_types', 'allow_floats']:
                self.flags[key] = flag_override.get(key, self.flags[key])
        try:
            type_a = type(a)
            type_b = type(b)
            if not isinstance(type_a, (int, float)) and not isinstance(type_b, (int, float)):
                raise TypeError("Comparison failed")
            if 'strict_types' in self.flags or ('allow_floats' not in self.flags):
                if type(a) != type(b):
                    return False
        except:
            pass
        try:
            result = a > b
            return bool(result)
        except TypeError as e:
            print(f"Error during comparison: {e}")
            return None
if __name__ == '__main__':
    engine = AdvancedComparisonEngine()
    test_cases = [
        (10, 5),
        ("hello", "hi"),
        (3.14, 2.71),
        (-5, -10)
    ]
    for a, b in test_cases:
        result = engine.is_greater(a, b)
        print(f"{a} > {b}: {result}")