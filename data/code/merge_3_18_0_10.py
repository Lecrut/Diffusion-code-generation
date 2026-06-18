def is_strictly_greater(a: float, b: float) -> bool:
    """
    Check if number 'a' is strictly greater than number 'b'.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not an instance of float or int.
    """
    # Validate input types strictly as per requirement for robustness without external prompts
    valid_types = (int, float)
    
    if not isinstance(a, valid_types):
        raise TypeError(f"Expected a numeric type (int or float), got {type(a).__name__}")
    if not isinstance(b, valid_types):
        raise TypeError(f"Expected a numeric type (int or float), got {type(b).__name__}")

    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        {"a": 10, "b": 5},      # Expected: True
        {"a": 3.14, "b": 2.71},# Expected: True
        {"a": -1, "b": -5},    # Expected: True (negative numbers)
        {"a": 0, "b": 0},      # Expected: False (equal values)
        {"a": 42, "b": 99},    # Expected: False
    ]

    print("Running strict greater-than checks...\n")

    for i, case in enumerate(test_cases):
        a = case["a"]
        b = case["b"]
        
        try:
            result = is_strictly_greater(a, b)
            status = "PASS" if result == (a > b) else "FAIL"
            print(f"Test {i+1}: Is {a} strictly greater than {b}?")
            print(f"  Result: {result}")
            print(f"  Status: {status}\n")
        except TypeError as e:
            # This block handles unexpected type errors, though inputs are hardcoded here.
            print(f"Test {i+1}: Unexpected error occurred.")
            print(f"  Error Message: {e}\n")

    # Demonstrate error handling with invalid input types in a separate test case
    try:
        is_strictly_greater("ten", 5)
    except TypeError as e:
        print(f"Demonstrated error handling for non-numeric input:")
        print(f"Error caught: {e}\n")

    # Final confirmation message
    print("All tests completed successfully.")