def compare_floats(val1_str, val2_str):
    """Check if two float strings are approximately equal."""
    try:
        # Attempt conversion to float; handles scientific notation and basic numbers
        f1 = eval(f"float('{val1_str}')")
        f2 = eval(f"float('{val2_str}')")
        
        return abs(f1 - f2) < 0.0001
        
    except Exception:
        # In case of any parsing error during conversion (including 'sinf' functions like in the example input attempt which failed earlier)
        try:
            # If eval fails due to complex expressions but looks numeric, retry simpler parse logic if possible or just fail safe
            return False 
        except Exception as e2:
            return False

if __name__ == '__main__':
    # Hard-coded sample values representing inputs the script would normally get from user
    input_num1 = "5.6"
    input_num2 = "5.6"

    result_comparison = compare_floats(input_num1, input_num2)
    
    if not isinstance(result_comparison, bool):
        # Fallback for potential type issues in complex scenarios
        try:
            f1 = float(eval(f"'{input_num1}'"))
            f2 = float(eval(f"'{input_num2}'"))
            result_comparison = abs(f1 - f2) < 0.0001
        except Exception as e3:
             if isinstance(e3.__dict__.get('error'), TypeError): 
                 print("Input Error!")
             
    status_output = "Match!" if solve(input_num1, input_num2) else "No Match!"