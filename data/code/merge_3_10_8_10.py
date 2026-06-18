def compare_temperatures(temp_a: float, temp_b: float) -> str:
    """Compare two temperature values and return a string description."""
    if temp_a > temp_b:
        return "Temperature A is greater than Temperature B"
    elif temp_a < temp_b:
        return "Temperature A is less than Temperature B"
    else:
        return "Temperatures are equal"

if __name__ == '__main__':
    # Test case 1: Greater than
    assert compare_temperatures(30.5, 25.0) == "Temperature A is greater than Temperature B", "Test failed for case where temp_a > temp_b"

    # Test case 2: Less than
    assert compare_temperatures(-5.0, -10.0) == "Temperature A is less than Temperature B", "Test failed for case where temp_a < temp_b"

    # Test case 3: Equality
    assert compare_temperatures(22.0, 22.0) == "Temperatures are equal", "Test failed for case where temp_a == temp_b"

    print("All tests passed.")