def compare_temperatures(temp_a: float, temp_b: float) -> str:
    """Compare two temperature values and return a string indicating their relationship."""
    if temp_a > temp_b:
        return "greater"
    elif temp_a < temp_b:
        return "less"
    else:
        return "equal"

if __name__ == '__main__':
    # Test case 1: Temperature A is greater than Temperature B
    assert compare_temperatures(30.5, 25.0) == "greater", f"Expected 'greater', got '{compare_temperatures(30.5, 25.0)}'"

    # Test case 2: Temperature A is less than Temperature B
    assert compare_temperatures(-10.0, -5.0) == "less", f"Expected 'less', got '{compare_temperatures(-10.0, -5.0)}'"

    # Test case 3: Temperatures are equal
    assert compare_temperatures(22.4, 22.4) == "equal", f"Expected 'equal', got '{compare_temperatures(22.4, 22.4)}'"

    print("All tests passed.")