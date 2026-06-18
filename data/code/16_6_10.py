def determine_positivity(num):
    """Returns a boolean indicating if num is positive."""
    return num > 0

if __name__ == '__main__':
    # Test cases: positive, negative, and zero inputs
    assert determine_positivity(5) is True
    assert determine_positivity(-3) is False
    assert determine_positivity(0.0) is False
    assert determine_positivity(1e-9) is True
    print("All tests passed.")