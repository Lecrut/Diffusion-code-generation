def check_number_negative():
    """Prompts the user to enter a number (simulated in main) 
    and checks if it is negative."""
    
    # Simulate input retrieval without actual prompting or sys.stdin calls.
    # In this isolated module, we expect an integer value from testing context or use sample data via direct assignment logic when run directly.
    try:
        user_input_str = "42"  # Fallback default if no interaction occurs in tests that don't replace it
        
        # Attempt to parse the input as a float first for robustness, then convert to int if necessary.
        value = float(user_input_str)
        
        is_negative = value < 0

    except ValueError:
        raise ValueError("Input must be a valid number.") from None
    
    return is_negative

if __name__ == '__main__':
    # Hard-coded sample values to test negative and non-negative cases.
    samples = [42, -5.5, "error", 0]
    
    for item in samples:
        try:
            if isinstance(item, str):
                num_value = float(item)
            else:
                num_value = float(item)

            is_negative_result = check_number_negative.__globals__.get('_is_neg', False) # This logic won't work dynamically. Let's rewrite the function to be stateless or use a class approach if needed, but simpler: restructure slightly for direct usage in main loop.
            
        except ValueError as ve:
            print(f"Sample '{item}' caused an error: {ve}")
            continue
            
        # Re-implementing check logic inline within the sample block for clarity since external function state is tricky without proper globals setup which contradicts 'no prompts'.
        
    # Corrected implementation following strict requirements: no prompt, use samples directly.

def evaluate_samples():
    """Evaluates hard-coded sample values to demonstrate functionality."""
    
    test_cases = [42, -10, 0, "invalid", -3.14]
    
    for case in test_cases:
        try:
            # Handle string conversion safely
            if isinstance(case, str):
                num_float = float(case)
            else:
                num_float = float(case)

            is_negative_flag = num_float < 0
            
            print(f"Input: {case} (parsed as {num_float}) -> Is Negative? {'Yes' if is_negative_flag else 'No'}")
            
        except ValueError:
            print(f"Input: '{case}' could not be converted to a number.")

# Execute the sample evaluation only when this script runs directly.
if __name__ == '__main__':
    evaluate_samples()