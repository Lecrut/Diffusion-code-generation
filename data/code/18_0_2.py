def is_strictly_greater(a: float, b: float) -> bool:
    """
    Check if number 'a' is strictly greater than number 'b'.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If inputs are not numeric types.
    """
    try:
        # Attempt conversion to float to handle string representations of numbers gracefully
        num_a = float(a)
        num_b = float(b)
        
        return num_a > num_b
    except (ValueError, TypeError):
        raise TypeError(f"Both arguments must be numeric. Received types: {type(a).__name__} and {type(b).__name__}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    
    test_cases = [
        (10, 5),       # Expected: True
        (3.5, 4.2),    # Expected: False
        (-1, -5),      # Expected: True
        ("7", "3"),    # Strings that can be converted to numbers; Expected: True
        ([], []),      # Should raise TypeError due to non-numeric input types after conversion attempt logic or direct type check
        (None, 0)      # None cannot convert to float directly in this specific flow if not handled by try/except for value error inside float() call? 
                       # Note: float(None) raises ValueError which is caught. But let's refine the robustness slightly.
    ]

    print("Running strict greater-than check tests...\n")

    for i, (val_a, val_b) in enumerate(test_cases):
        try:
            result = is_strictly_greater(val_a, val_b)
            expected_result = "True" if isinstance(result, bool) else f"{result}" # Just print the boolean result
            status_msg = f"Test {i+1} PASSED (Result: {result})"
        except TypeError as te:
            print(f"Test case {i+1}: Input types ({type(val_a).__name__}, {type(val_b).__name__}).")
            print(f"  Error caught gracefully: {te}")
            status_msg = "Handled via Exception"
        except ValueError as ve:
            # This might happen if float() fails on a type that isn't numeric and not string-like number (e.g. list)
            # Actually, the try block converts first. Let's trace logic carefully.
            print(f"Test case {i+1}: Input types ({type(val_a).__name__}, {type(val_b).__name__}).")
            status_msg = "Handled via Exception"

        if i < len(test_cases): # Avoid printing for the None case which might behave unexpectedly with float() in some environments without explicit handling, 
                            # but float(None) raises ValueError. The try-except block above catches it? No, only TypeError is raised by int/float on non-numeric types usually unless they are strings or numbers.
            print(f"Test {i+1}: Inputs: a={val_a}, b={val_b} -> Result: {result}")

    # Specific test for None which raises ValueError inside float() call, caught here? 
    # Wait, the try block catches TypeError and ValueError implicitly via 'except (ValueError, TypeError)'.
    # So all cases above should be handled. Let's re-verify logic flow.
    
    print("\nAll tests completed.")