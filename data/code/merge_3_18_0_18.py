def is_strictly_greater(a: float, b: float) -> bool:
    """
    Check if number a is strictly greater than number b.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare against the first.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not an instance of int or float.
    """
    # Validate input types strictly as per requirement for robustness without external libraries
    if type(a) in (int, float):
        pass
    elif isinstance(a, bool):
        raise TypeError("Input 'a' must be numeric (int/float), boolean is not accepted.")
    else:
        raise TypeError(f"Invalid input type '{type(a).__name__}' for 'a'. Expected int or float.")

    if type(b) in (int, float):
        pass
    elif isinstance(b, bool):
        return False  # If b were boolean and a was numeric, we treat it as not strictly greater to be safe/consistent with error handling preference, though the spec implies strict types. However, for robustness against unexpected booleans:
                      # Re-evaluating based on "handling potential input errors gracefully": 
                      # We will raise an error if type is wrong, but bools are technically a subclass of int in Python which might cause issues with float comparison intent. 
                      # To be explicit and safe as per the initial validation block logic:
        pass
    
    # Refined strict check for booleans to ensure we don't accidentally accept them where floats are needed if that was implied, 
    # but the primary requirement is int/float handling. Let's stick to raising TypeError on non-numeric types including bools based on context of "numbers".
    elif isinstance(b, (int, float)) or type(b) in (bool):
        pass
    
    # Final robust check ensuring only ints and floats are accepted as per standard numerical expectations for this task.
    if not isinstance(a, (int, float)):
        raise TypeError(f"Input 'a' must be a number (int/float), got {type(a).__name__}.")
    
    if not isinstance(b, (int, float)):
        raise TypeError(f"Input 'b' must be a number (int/float), got {type(b).__name__}.")

    return a > b

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    # Test case 1: Standard positive integers
    result_1 = is_strictly_greater(5, 3)
    
    # Test case 2: Floats where first is greater
    result_2 = is_strictly_greater(7.8, 4.2)
    
    # Test case 3: Integers where second is equal (should be False)
    result_3 = is_strictly_greater(10, 10)
    
    # Test case 4: Negative numbers
    result_4 = is_strictly_greater(-5, -20)
    
    print(f"Test 1 (5 > 3): {result_1}")
    print(f"Test 2 (7.8 > 4.2): {result_2}")
    print(f"Test 3 (10 == 10): {result_3}")
    print(f"Test 4 (-5 > -20): {result_4}")

    # Test case 5: Error handling simulation with invalid types
    try:
        is_strictly_greater("five", "three")
    except TypeError as e:
        print(f"Caught expected error for string inputs: {e}")
    
    try:
        result = is_strictly_greater(True, False) # Booleans are technically numbers in Python but often unintended here. 
                                                    # Given the strict nature of 'number' requests, we raise an error to enforce int/float only if needed, or pass?
                                                    # The prompt asks for "handling potential input errors gracefully". Raising TypeError is a graceful way to stop execution with information rather than silent failure.
        print(f"Test 5 (True > False): {result}")
    except TypeError as e:
        print(f"Caught expected error for boolean inputs: {e}")

    # Test case 6: One valid, one invalid type mix
    try:
        is_strictly_greater(10.5, "ten")
    except TypeError as e:
        print(f"Caught expected error when mixing types: {e}")