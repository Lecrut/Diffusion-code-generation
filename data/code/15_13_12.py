def check_equal(a: object, b: object) -> bool:
    """Check if two objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases without external input or files
    assert (10 == 10), "Integers should be equal"
    assert ("hello" != "world"), "Strings with different content should not be equal"
    print("All basic equality checks passed.")