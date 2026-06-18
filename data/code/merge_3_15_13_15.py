def check_equal(a: object, b: object) -> bool:
    """Check if two objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample values to test without user input or external dependencies
    obj1 = {"key": "value"}
    obj2 = {"key": "value"}
    obj3 = [1, 2, 3]
    obj4 = (1, 2, 3)

    assert check_equal(obj1, obj2) is True
    assert check_equal(obj3, obj4) is False
    print("All checks passed.")