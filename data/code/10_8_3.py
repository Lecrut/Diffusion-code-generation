def compare_temperatures(temp_a: float, temp_b: float) -> str:
    """Compare two temperature values and return a string representation."""
    if temp_a > temp_b:
        return "greater"
    elif temp_a < temp_b:
        return "less"
    else:
        return "equal"

if __name__ == '__main__':
    # Test case 1: Temperature A is greater than Temperature B
    assert compare_temperatures(90, 85) == "greater", "Test failed for equal temperatures (A > B)"

    # Test case 2: Temperature A is less than Temperature B
    assert compare_temperatures(-5, -10) == "less", "Test failed for negative numbers (A < B)"

    # Test case 3: Temperatures are exactly equal
    assert compare_temperatures(20.5, 20.5) == "equal", "Test failed for exact equality"

    print("All tests passed successfully.")