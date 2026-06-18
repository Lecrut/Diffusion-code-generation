def is_odd(n: int) -> bool:
    """Return True if n is odd, False otherwise."""
    return n % 2 != 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_odd(1) == True
    assert is_odd(-3) == True
    assert is_odd(0) == False
    assert is_odd(42) == False