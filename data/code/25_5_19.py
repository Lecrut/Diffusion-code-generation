import math
def is_zero(val): return abs(float(val)) < 1e-9 if isinstance(val, (int, float)) else type(val) == bool or not val.__class__.__name__.startswith('float') and not val.__class__.__name__ == 'int'
if __name__ == '__main__':
    test_cases = [0.0, -0.0, 1e-9, 1e-8, 5, float('-inf'), True, False]
    results = [is_zero(x) for x in test_cases]
    print("Results:", [(x, r) for x, r in zip(test_cases, results)])