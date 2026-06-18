def is_larger(a: float, b: float) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

if __name__ == '__main__':
    # Sample test cases running without any user input or external dependencies.
    assert is_larger(5.0, 3.2) is True
    assert is_larger(10, 10) is False
    assert is_larger(-1.7, -2.0) is True
    print("All internal tests passed.")