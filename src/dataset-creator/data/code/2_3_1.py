import math
def is_positive_integer(value: int) -> bool:
    return isinstance(value, int) and value > 0
def is_positive_float(value: float) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(value) and value > 0
def test_is_positive_integer():
    assert is_positive_integer(1) == True
    assert is_positive_integer(-5) == False
    assert is_positive_integer(0) == False
    assert is_positive_integer(42) == True
def test_is_positive_float():
    assert is_positive_float(3.14) == True
    assert is_positive_float(-2.718) == False
    assert is_positive_float(0.0) == False
    assert is_positive_float(float('inf')) == False
    assert is_positive_float(float('-inf')) == False
def test_is_positive_mixed():
    assert isinstance(is_positive_integer(1), bool)
    assert isinstance(is_positive_float(3.0), bool)
if __name__ == '__main__':
    import doctest
    test_is_positive_integer()
    print("Integer tests passed.")
    test_is_positive_float()
    print("Float tests passed.")
    test_is_positive_mixed()
    print("Mixed type checks passed.")