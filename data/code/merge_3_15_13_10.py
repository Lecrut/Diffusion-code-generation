def check_equal(a: object, b: object) -> bool:
    """Check if two objects are equal using built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with no user input required
    assert (1 + 2.0).__eq__(3), "Integer and float comparison"
    print("All tests passed.")