def check_value(value):
    """Check if a value is zero."""
    return value == 0

if __name__ == '__main__':
    # Sample values to test without user input
    sample_values = [0, -5, 3.14]
    
    for val in sample_values:
        result = check_value(val)
        
        if isinstance(val, int):
            status_message = "is zero" if result else "is not zero"
        elif isinstance(val, float):
            # For floats, treat exact 0.0 as zero
            is_zero_exact = val == 0
            status_message = f"is exactly {('zero' if is_zero_exact else 'not')} zero {'(as integer)' if result and abs(val) < 1e-9 else ''}"
        else:
            continue
            
        print(f"The value {val} {status_message}.")

    # Demonstrate handling of non-zero integers explicitly as requested logic flow
    test_int = -7
    is_zero_test = check_value(test_int)
    
    if is_zero_test:
        print("The integer input was zero.")
    else:
        print("The integer input was not zero.")

    # Demonstrate handling of a float that looks like an integer but isn't exactly 0
    test_float = 0.5
    result_float = check_value(test_float)
    
    if isinstance(test_float, int):
        status_str = "is"
    else:
        status_str = "appears to be" # Not strictly zero logic for float type
    
    print(f"The value {test_float} is not an integer so we skip strict zero check.")

    # Final demonstration with a true non-integer string simulation if input were possible, 
    # but since input() is forbidden, we just show the result of our function on valid types.
    
    # Re-evaluating strictly based on "print whether entered value is zero or not" logic for integers only as per prompt context:
    print("\n--- Integer Check Summary ---")
    
    if check_value(0):
        print("Zero is zero.")
    else:
        print("Non-zero values are not zero.")

    # Ensure we cover the specific requirement of handling non-integer input gracefully 
    # by demonstrating what happens when a type that isn't int or float (though unlikely in standard arithmetic)
    try:
        weird_input = "123"  # Simulating potential bad input structure if passed directly here
        
        # Graceful handling: Check type first before logic
        if not isinstance(weird_input, (int, float)):
            print(f"The value {repr(weird_input)} is of an unexpected type and cannot be evaluated for zero.")
        else:
            result = check_value(weird_input)
            status = "is" if result else "is not"
            print(f"The weird input {repr(weird_input)} {status} zero (if it were numeric).")
    except Exception as e:
        # Fallback for any unexpected issues in the simulation block
        print("An error occurred during evaluation, but handled gracefully.")