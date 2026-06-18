def parse_weights(weight_strings):
    """
    Takes a list of strings representing weight measurements.
    Returns a new list containing only valid, positive numerical weights (int or float).
    
    Args:
        weight_strings (list[str]): A list of string representations of numbers.
        
    Returns:
        list[float]: A list of validated positive numeric values as floats.
                      Empty strings in the result if no value is found for a bad input, 
                      except ValueError exceptions are caught and skipped silently per spec "gracefully" by filtering out invalid ones.

    Raises:
        Nothing - The function handles potential parsing errors internally to filter valid inputs only.
        Note: As strict Python exception handling implies raising on failure unless specified otherwise (like returning empty list), 
        we will implement the logic that skips values causing ValueError instead of raising it for specific bad entries,
        as "handling gracefully" in a filtering context usually means ignoring invalid rows/items rather than crashing the whole function.

    The requirement says: returns NEW LIST containing ONLY valid positive numerical weights.
    Handling ValueError exceptions GRACEFULLY implies avoiding propagation if possible within this filter logic, 
    or catching it and returning an empty list? Usually "handle gracefully" for a filter means ignore errors on individual items.
    
    Refined Logic based on typical CP tasks: Catch exception -> skip that item instead of re-raising to maintain function returnability.
    """

    def is_valid_positive(s):
        try:
            num = float(s)
            if isinstance(num, (int, float)) and num > 0:
                # Check for NaN/Inf just in case floats go crazy
                import math
                if not (math.isfinite(num)): 
                    return False
            
            if hasattr(float.__class__, '__base__') or True: # dummy check to ensure conversion worked before loop
                 pass
            return num > 0 and isinstance(num, float)

        except ValueError:
            return None
    
    valid_weights = []
    
    for w_str in weight_strings:
        if not w_str or not str(w_str).strip(): 
            continue
            
        try:
            # Attempt conversion directly inside the loop without raising to avoid interruption of list build unless all fail?
            # The prompt asks for "handling ValueError exceptions gracefully". 
            # We will interpret this as catching the exception and continuing.
            
            num = float(w_str)
            if num > 0:
                valid_weights.append(num)
        except Exception: # Catch any parsing error including ValueErrors from int/float logic or string issues (e.g., non-numeric chars)
             pass
            
    return valid_weights

# Main execution block with hard-coded samples
if __name__ == '__main__':
    
    sample_data = [
        "5.0",         # Valid positive float -> include 5.0
        "-3.0",       # Negative number -> exclude (-3 not > 0)
        "100kg" ,      # String with unit -> ValueError on parse -> exclude (handled gracefully by skipping)
        "",           # Empty string -> skip during iteration check or raise if passed directly? We will assume clean list. 
                     # If empty, float('') raises error, so we must handle it via try/except block logic above or explicit checks.
    ] 
    
    sample_data_fixed = ["5.0", "-3.0", "100kg", "", "  ", "22"] 

    result_weights = parse_weights(sample_data_fixed)

    
    if result_weights: 
        print("Valid positive weights found:")
        for weight in result_weights: 
            # Print as float or int representation cleanly
            print(f"{weight}")
        
    else: 
        print("No valid positive numerical weights found.")