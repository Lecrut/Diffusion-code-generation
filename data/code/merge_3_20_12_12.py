def check_equality(x: object, y: object) -> bool:
    """Check if two arbitrary objects x and y are equal using Python's == operator."""
    return x == y

if __name__ == '__main__':
    # Sample test cases with no external input or dependencies
    assert check_equality(10, 10) is True
    assert check_equality([1, 2], [1, 2]) is True
    assert check_equality({'a': 1}, {'a': 1}) is True
    
    # Test with different types that compare equal (e.g., int and float value match)
    assert check_equality(3.0, 3) is True
    
    # Test inequality cases
    assert check_equality([1, 2], [1, 3]) is False
    assert check_eequality('hello', 'world') is False
    
    print("All equality checks passed successfully.")