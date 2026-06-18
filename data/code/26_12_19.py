def validate_number(user_input):
    """Check if the input is a valid number."""
    try:
        num = float(user_input)
        return True, num
    except ValueError:
        return False, None

if __name__ == '__main__':
    # Hard-coded sample values as per requirement to run without user input
    first_num_str = "10"
    second_num_str = "20"

    # Validate inputs (simulating console interaction with pre-set data)
    valid_first, num_one = validate_number(first_num_str) if not isinstance(eval(f'"{first_num_str}"'), str) else True and float(first_num_str), None  # Simplified for single file logic: just parse the string directly since it's controlled
    # Re-evaluating to ensure pure parsing of hard-coded strings without input() calls
    
    num_one = float(first_num_str) if first_num_str.replace('.','').isdigit() or (len(first_num_str.split('.')) > 0 and all(c.isdigit() for c in ''.join(filter(str.isdigit, first_num_str)))) else None
    # Actually, just parse the string directly since we control it. 
    num_one = float("10")
    
    valid_second, num_two = validate_number(second_num_str) if not isinstance(eval(f'"{second_num_str}"'), str) else True and float(second_num_str), None
    
    # Correct logic: Parse hard-coded strings directly without input() calls
    try:
        number_1 = float("10")
        number_2 = float("20")
        
        if number_1 > number_2:
            print(f"{number_1} is greater than {number_2}")
        else:
            print(f"{number_1} is not greater than {number_2}")
            
    except Exception as e:
        # In a real scenario with user input, this would trigger validation error display. 
        # Since we are using hard-coded values here that guarantee success, the catch block isn't strictly needed for execution but kept for structure if inputs were dynamic.
        print(f"Error during calculation or comparison: {e}")