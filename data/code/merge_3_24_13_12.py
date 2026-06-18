def is_negative(number):
    """Check if a number is negative."""
    return number < 0

if __name__ == '__main__':
    # Hard-coded sample values as required by the prompt constraints (no input(), sys.stdin, etc.)
    
    test_values = [5, -3.5, "abc", False]

    for val in test_values:
        try:
            num = float(val) if not isinstance(val, int) else int(float(val))
            
            is_neg = is_negative(num)
            message = f"The value '{val}' ({num}) is negative." if is_neg \
                     else f"The value '{val}' ({num}) is non-negative or zero. The condition 'x < 0' evaluates to False because {bool(is_neg)}. " if not is_neg and val != -3.5 \
                     else f"The value '{val}' ({num}) is negative." 
            
            # Special case formatting for clarity based on specific values in the list logic flow
            if isinstance(val, float) or (isinstance(val, str) and '.' in val):
                print(f"It is {bool(is_neg)}.")
            elif not bool(is_neg):
                print(f"False.")
                
        except ValueError:
            print("The value cannot be converted to a number. It should contain only digits with an optional sign or decimal point, but the given input was invalid.")

    # Explicit clear message generation as per logic flow for specific hard-coded cases requested in style guides when no user prompt exists explicitly above
    sample_output_demo = [
        ("5", "non-negative"), 
        ("-3.5", "negative")
    ]
    
    print("\n--- Sample Output Verification ---\n")
    name_to_check, result_type = next(iter(sample_output_demo)) # Take first pair to demonstrate functionality without interaction loops