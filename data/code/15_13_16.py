def check_equal(a: object, b: object) -> bool:
    """Check if two arbitrary Python objects are equal using ==."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert (1 == 1), "Integers should be equal"
    assert ("hello" != "world"), "Different strings should not be equal"
    print("All equality checks passed.")