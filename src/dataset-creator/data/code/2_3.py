import math
def is_positive_int(value: int) -> bool:
    return isinstance(value, int) and value > 0
def is_positive_float(value: float) -> bool:
    return isinstance(value, float) and math.isfinite(value) and value > 0
def test_is_positive_int():
    assert is_positive_int(1) == True
    assert is_positive_int(-5) == False
    assert is_positive_int(0) == False
    assert is_positive_int(42) == True
def test_is_positive_float():
    assert is_positive_float(3.14) == True
    assert is_positive_float(-9.8) == False
    assert is_positive_float(0.0) == False
    assert is_positive_float(math.inf) == False
    assert is_positive_float(float('nan')) == False
def run_tests():
    test_is_positive_int()
    test_is_positive_float()
    print("All tests passed.")
if __name__ == '__main__':
    sample_values = [1, -5, 0.34, float('-inf'), math.inf]
    results = {v: is_positive_int(v) if isinstance(v, int) else is_positive_float(v) for v in sample_values}
    print("Sample Results:")
    for val, res in results.items():
        print(f"Value: {val}, Is Positive: {res}")
    test_is_positive_int()
    test_is_positive_float()