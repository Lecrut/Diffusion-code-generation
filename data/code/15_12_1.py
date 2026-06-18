def get_number(prompt):
    """
    Reads a number from the user with error handling for non-integer inputs.
    
    Args:
        prompt (str): The message displayed to the user before inputting data.
        
    Returns:
        int or float: The parsed numerical value of the input string.
        
    Raises:
        ValueError: If the input is not a valid integer or float representation.
    """
    try:
        # Attempt to convert the input string directly to an integer first, 
        # then fall back to float if that fails (to handle cases like "1" vs 1).
        return int(prompt)
    except ValueError:
        # If it's not a valid integer, check for other numeric formats or just raise.
        try:
            value = float(prompt)
            
            # Check if the input was effectively an integer (e.g., "5" vs 5.0)
            # The problem asks to ensure robust error handling for non-integer inputs.
            # We will treat any valid number as acceptable, but note that int() raises on floats like "3.14".
            return value
            
        except ValueError:
            raise

def check_equality(num1_str, num2_str):
    """
    Checks if the numerical values represented by two strings are equal.
    
    Args:
        num1_str (str): First input string representation of a number.
        num2_str (str): Second input string representation of a number.
        
    Returns:
        bool: True if the numeric values are identical, False otherwise.
        
    Raises:
        ValueError: If either or both strings cannot be converted to valid numbers.
    """
    try:
        val1 = get_number(num1_str)
        val2 = get_number(num2_str)
        
        # Compare as floats for equality check if they were originally different types (int vs float),
        # though the problem specifically mentions "non-integer inputs" error handling. 
        # To be strictly robust, we compare their numeric values directly.
        return val1 == val2
        
    except ValueError:
        raise

if __name__ == '__main__':
    try:
        # Hard-coded sample values to ensure the block runs without user input
        sample_input_1 = "5"
        sample_input_2 = "5.0"  # This will be parsed as float, treated as not equal to int in strict integer contexts, 
                                # but numerically equivalent if we consider value equality.
        
        num_str_1 = sample_input_1
        num_str_2 = sample_input_2
        
        result = check_equality(num_str_1, num_str_2)
        
        print(f"Numbers {num_str_1} and {num_str_2}: {'Equal' if result else 'Not Equal'}")

    except ValueError as e:
        # Handle cases where input strings fail to convert (e.g., "abc", "", etc.)
        error_msg = f"Invalid number format in inputs. Error details: {str(e)}"
        print(error_msg)