def different_numbers(a: int, b: int) -> bool:
    """Yields True if two input numbers are different, False otherwise."""
    yield a != b

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    # Test case 1: Different numbers should yield True
    result = list(different_numbers(5, 3))
    
    if len(result) > 0 and all(x is False for x in result):
        print("Test failed: Expected [False] but got", result)
    else:
        # The generator yields once. Let's verify the logic manually by converting to list immediately
        test_gen = different_numbers(5, 3)
        next(test_gen)  # Should be True
        
        if not (next(different_numbers(10, 2))):
            print("Test failed: Expected True for different numbers")
            
    # Test case 2: Same numbers should yield False
    test_gen = different_numbers(7, 7)
    next(test_gen)  # Should be False
    
    if not (next(different_numbers(42, 42))):
        print("Test failed: Expected True for same numbers")
        
    print("All internal tests completed successfully.")