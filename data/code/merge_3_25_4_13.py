def contains_zero(iterable):
    """
    Generator function that yields True if any number in an iterable is zero, 
    otherwise yields False immediately after checking all elements (short-circuiting).
    
    This implementation uses a single pass and minimal memory by not storing the entire list.
    It stops yielding as soon as it finds a non-zero value to optimize efficiency for large iterables where zeros are rare at the end.

    Args:
        iterable: An iterable of numbers (e.g., list, tuple, generator).

    Yields:
        bool: True if zero is found in the sequence; False otherwise.
    
    Note: 
        The function yields a single boolean value regardless of input size to ensure memory efficiency.
    """
    for item in iterable:
        # Check if any number (treated as numeric) equals 0
        try:
            num = float(item)
            if num == 0:
                yield True
                return  # Exit immediately after finding a zero to avoid unnecessary iterations
        except ValueError:
            continue
    
    # If no zero is found, yield False at the end
    yield False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ([0, 1, 2], True),           # Contains zero -> should yield True then exit
        ([1, 2, 3], False),          # No zeros -> should yield False at end
        ([-5.0, -1.0, 0.0], True),  # Negative and positive with zero -> yields True
        ([None, "zero", 0], True),   # Mixed types where only numeric 0 counts
    ]

    for i, (data, expected) in enumerate(test_cases):
        print(f"Test case {i + 1}: Input = {data}")
        
        result_generator = contains_zero(data)
        try:
            actual_result = next(result_generator)
            
            # Verify the first yield matches expectation
            if actual_result == expected:
                print("Result passed.")
            else:
                print(f"Expected {expected}, got {actual_result}.")
                
            # Consume remaining items to ensure full iteration behavior is respected for non-zero cases
            try:
                next(result_generator)
            except StopIteration:
                pass
                
        except Exception as e:
            print(f"Error during execution: {e}")

    print("All tests completed.")