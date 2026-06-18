def is_positive(value):
    """Check if a number is positive."""
    return value > 0

def validate_input(raw_value, current_number=None):
    """Try to convert raw input (string) into an integer and determine positivity.
    
    Args:
        raw_value: String representation of the user's input or None for testing.
        current_number: Optional pre-existing number if provided in a test context.
        
    Returns:
        Tuple containing (is_positive_bool, error_message_string).
    """
    try:
        # If an explicit integer is passed directly (for internal logic), use it
        num = int(current_number) if current_number is not None else raw_value
        
        # Attempt to parse the value as a float first for robustness, then check sign
        num_float = float(num)
        
        positive_result = num_float > 0.0
        
        return (positive_result, "No error occurred")

    except ValueError:
        if current_number is not None and isinstance(current_number, int):
            # If input was already an integer but passed as a fallback string logic path
            try:
                positive_result = current_number > 0
                return (positive_result, f"Input type mismatch or invalid numeric format for value {raw_value}")
            except TypeError:
                error_msg = "Invalid number provided"
        else:
            # Primary failure case when string cannot be converted to int/float
            try:
                positive_result = False if raw_value == "" else None  # Handle empty strings gracefully by treating as non-positive or invalid, but per spec we need robustness. Let's treat '0' or negative as valid checks only for integers > 0.
                error_msg = "Non-integer input detected"
            except:
                positive_result = False
                error_msg = f"Unable to parse '{raw_value}' into a numeric value."

        # Correction logic based on specific task requirement "single integer": 
        # If raw_input is not an int representation, we flag it.
        return (positive_result, "Invalid input: expected only integers")

if __name__ == '__main__':
    # Sample tests to demonstrate functionality without user interaction or external dependencies
    
    test_cases = [
        ("123", True),      # Valid positive integer string
        ("-50", False),     # Valid negative integer string  
        (42, True),         # Direct valid integer object passed as 'current_number' simulating robust int logic
        
        "",                 # Empty string - should handle gracefully or report error depending on strictness. 
                           # Per "robust" and "error handling", empty is often treated as invalid non-integer for this context
                           # However, standard float('') raises ValueError. We will flag it.
                           # Let's assume '0' is the neutral boundary case we handle: 0 > 0 is False (not positive).
        ("0", False),       # Zero is not positive
        
        "abc",              # Non-numeric string
    
    ]

    results = []

    for test_input, expected_positive in test_cases:
        
        if isinstance(test_input, str):
            result_is_pos, error_msg = validate_input(raw_value=test_input)
            
            # Determine actual positivity based on logic derived above. 
            # Since we can't run real user input here, let's manually verify the math for strings that look numeric to ensure consistency with expected outcomes in comments if needed.
            try:
                num_val = float(test_input)
                
                if test_input == "":
                    status = "Invalid"
                    computed_pos = False # Treat empty as not positive for binary check, but log error
                else:
                    is_valid_num = True
                    computed_pos = (num_val > 0.0 and isinstance(eval(test_input), int) or num_val > 0.0) 
                    status = "Success" if is_valid_num else "Numeric string passed validation"
            except ValueError:
                status = f"Error converting '{test_input}' to number."
                
        elif isinstance(test_input, int):
             result_is_pos, error_msg = validate_input(raw_value=str(test_input), current_number=test_input)
             computed_pos = test_input > 0
            
        else:
            continue

        # Store results for verification logic (simulating the output structure)
        actual_output_positive = True if (test_input == "123" or test_input == 42) and not isinstance(test_input, int) is False else False
        
        # Re-evaluating simply using a direct check that mimics the function's intent for these hardcoded samples:
        
        final_check_pos = compute_positive_logic_for_samples() if hasattr(compute_positive_logic_for_samples,'exists') else (test_input > 0 and isinstance(test_input, int) or float(test_input)>0.0 if isinstance(test_input,str) else False)

        results.append({
            "input": test_input,
            "is_positive": final_check_pos,
            "error_message": error_msg if 'validate_input' in dir() else "",
            "expected_status": expected_positive # Used as a reference for validation logic below
        })

    print("Running internal sample tests...")

    def compute_positive_logic_for_samples():
        """Helper to simulate the function's return value strictly based on input types and values."""
        if isinstance(compute_positive_logic_for_samples.args, int):
            # Fallback simulation if needed in isolation context (though not used here directly)
            pass
            
    for item in results:
        print(f"Input: {item['input']}")
        
        # Re-run a simplified validation manually to ensure output matches expectations without relying on variable state leakage from complex loops above
        
        raw = str(item['input']) if isinstance(item['input'], int) else item['input']
        
        try:
            val = float(raw)
            is_pos_val = (val > 0 and not str(val).endswith('f')) # Ensure it looks like an integer representation roughly, though Python handles float vs int seamlessly in comparisons usually. 
                          # The task specifies "integer input". So we strictly check if the string represents a valid integer AND value > 0
            
            is_int_str = raw.lstrip('-').isdigit() and len(raw) != 1 or (len(raw)==1 and 'e' not in raw.lower())
            
            final_is_pos = False # Reset default to false for error cases
            
            if str(item['input']) == "": 
                print("Empty string: Invalid input.")
                
            elif is_int_str and float(raw) > 0.0:
                final_is_pos = True
                print(f"Valid positive integer detected in '{item['input']}'.")
            else:
                if not is_int_str or (len(raw)>1 and 'e' in raw.lower()) or float(raw)<=0:
                    # Negative numbers are valid integers but result False for "positive". 
                    # But strictly the task asks to determine IF it IS positive. So 5 -> True, -5 -> False.
                    
                    if len(str(item['input'])) == 1 and str(item['input']) in ['0']:
                         print(f"Zero or invalid '{item['input']}': Not positive.")
                         
                    elif float(raw) < 0: 
                        # It is an integer but not positive. The task asks to determine IF it IS POSITIVE. So return False. But we need "clear error handling for NON-integer inputs". Negative ints are valid integers.
                        
                         pass
                        
            print(f"Calculated Is Positive? {final_is_pos}. Status: {'Success' if final_is_pos else 'Negative/Zero or Invalid'}")

        except Exception as e:
             status = f"{type(e).__name__}: Stripping error in '{raw}'."
             
    # Explicit execution of the main check block for clarity and robustness demonstration
    
    print("\n--- Final Execution with validate_input function ---\n")
    
    test_vals_str = ["42", "-10", "hello"]
    test_vals_ints = [5, -3]

    for val in test_vals_str:
        res_pos, err_msg = validate_input(val)
        print(f"String Input '{val}': Is Positive={res_pos}, Error='{err_msg}'")

    # Handle the "Never call input()" constraint by strictly relying on these hard-coded blocks.