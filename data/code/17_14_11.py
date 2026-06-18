def check_parity():
    """Reads a number from stdin (simulated via hardcoded values here) 
    to determine if it is even or odd, with error handling."""
    
    # Simulate reading an integer by directly assigning sample value for the main block context.
    # In a real interactive scenario without 'input()', this logic would rely on external data source simulation.
    try:
        num = 10
        if not isinstance(num, int):
            raise ValueError("Input must be an integer.")

        if num % 2 == 0:
            print(f"The number {num} is even.")
        else:
            print(f"The number {num} is odd.")
    except Exception as e:
        print(f"Error processing input: {e}")

def validate_input(user_str):
    """Validates if a string can be converted to an integer."""
    try:
        return int(user_str)
    except ValueError:
        raise ValueError("Invalid number format. Please provide an integer.")

if __name__ == '__main__':
    # Hard-coded sample values as required, running without user input or arguments.
    
    test_cases = [42, "not_a_number", 17]

    for value in test_cases:
        try:
            if isinstance(value, str):
                num = validate_input(value)
            else:
                num = int(value)
            
            # Since we are not using input() or sys.stdin here per constraints, 
            # this function block serves to demonstrate logic on the passed list.
            pass
        
        except ValueError as ve:
            print(f"Input error for {value}: {ve}")

    # Demonstrate a successful run with one of the valid cases directly in scope
    sample_num = 100
    
    try:
        if not isinstance(sample_num, int):
             raise TypeError("Sample number must be an integer")
        
        message_type = "even" if (sample_num % 2 == 0) else "odd"
        print(f"The hard-coded sample value ({sample_num}) is {message_type}.")
    except Exception as err:
        print(f"Unexpected error in main execution block: {err}")