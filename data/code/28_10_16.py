def is_larger(a: float, b: float) -> bool:
    """Returns True if a is strictly greater than b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_larger(5.0, 3.0) is True
    assert is_larger(10, 20) is False
    assert is_larger(-1.5, -2.5) is True
    assert is_larger(float('inf'), float('-inf')) is True
    print("All tests passed.")