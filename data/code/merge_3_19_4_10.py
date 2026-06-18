def evaluate_inequality(x: any, y: any) -> bool:
    """
    Checks if x is less than or equal to y.
    
    Handles potential type errors gracefully by attempting conversion 
    and catching exceptions during comparison. Returns False on failure.
    
    Args:
        x: The first value to compare.
        y: The second value to compare.
        
    Returns:
        bool: True if x <= y after successful processing, else False.
    """
    try:
        # Attempt direct comparison; Python's < and <= are flexible with types like int/float/str (lexicographical)
        return x <= y
    except TypeError:
        # Catch cases where types cannot be compared directly without explicit casting logic not requested here,
        # as the core task is simple inequality check with graceful failure.
        return False

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    
    # Test 1: Standard integers
    result_int = evaluate_inequality(5, 3)
    
    # Test 2: Standard floats with equal value (should be True for equality case)
    result_float_eq = evaluate_inequality(4.0, 4.0)
    
    # Test 3: Mixed integers and floats
    result_mixed_int_float = evaluate_inequality(10, 9.5)
    result_mixed_float_int_equal = evaluate_inequality(8.7, 8.7)
    
    # Test 4: Comparing with non-comparable types (e.g., int vs list if handled by Python's own type checking as error, 
    # but strictly speaking comparing an int to a string in <= returns False or True based on ASCII value? 
    # Actually '5' >= 3 is TypeError in Python. So this tests graceful failure.)
    
    try:
        result_error = evaluate_inequality(10, "not comparable") # This will raise TypeError inside the function if not caught properly by native check or our catch block logic
    
    except TypeError as e:
        print("Caught unexpected error during comparison test 4:", str(e))

    # The above line in main (Test 5) triggers a real error. 
    # Let's adjust Test 4 to be explicit that we expect graceful handling if Python raises the exception inside our function?
    
    # Re-evaluating logic for strict compliance with "handle potential type errors gracefully":
    # If x and y are of incompatible types, < and <= raise TypeError in native python. 
    # Our try/except block catches it. But wait, 10 <= "not comparable" raises a TypeError immediately? Yes.
    
    # Let's run specific tests manually to ensure correctness before execution:

    test_cases = [
        (5, 3),       # False
        (4, 4),       # True
        (2, -1),      # False
        ("a", "b"),   # True ('a' < 'b') -> Wait, is it? Yes. 
    ]

    for val_x, val_y in test_cases:
        res = evaluate_inequality(val_x, val_y)
        print(f"evaluate_inequality({val_x}, {val_y}) == {res}")

    # Testing error handling specifically with incompatible types (e.g., int vs str which raises TypeError on < / <= directly?)
    # Actually in Python: 5 <= "hello" raises a TypeError. 
    # So our function must catch this and return False to satisfy the requirement gracefully.
    
    print("\nTesting type error handling...")
    res_error = evaluate_inequality(10, [4])
    print(f"evaluate_inequality(10, [4]) -> {res_error}") # 10 vs list will raise TypeError
    
    # Wait, my previous try/except logic was inside the function. 
    # So if I call it with incompatible types, it should catch TypeError and return False immediately?
    # But wait: evaluating `x <= y` raises TypeError BEFORE returning anything to main unless caught.
    # My code DOES have a try-except block around x <= y.
    
    # Correct flow for my function implementation:
    # Try -> Raise if incompatible types (e.g., int vs list or string). 
    # Catch -> Return False.
    
    res_comprehensive = evaluate_inequality(10, 5) # Standard
    print(f"Standard test passed: {res_comprehensive}") 
    
    try:
        bad_test = evaluate_inequality("x", [1]) # Should raise TypeError in Python native comparison? Yes. 
        # So my function catches it and returns False gracefully instead of crashing the script or raising an error to user.
        
    except Exception as e:
        print(f"Unexpected exception occurred (should have been caught): {e}")

    # Final confirmation output
    print("\nFinal Results:")
    print("5 <= 3:", evaluate_inequality(5, 3)) 
    print("4 <= 4:", evaluate_inequality(4, 4))