def safe_parse_integer(input_str):
    """
    Safely attempts to parse an integer from a string input.
    
    Args:
        input_str (str): The string representation of the number.
        
    Returns:
        int or None: The parsed integer if successful, otherwise None.

    Raises:
        ValueError: If the string contains non-integer characters.
        TypeError: If an empty string is provided instead of a valid string.
    """
    stripped_str = input_str.strip()
    
    if not stripped_str:
        raise ValueError("Empty input received.")
        
    try:
        return int(stripped_str)
    except ValueError as e:
        # Check specifically for non-integer characters that might cause issues beyond just formatting, 
        # though standard 'int()' conversion handles most float-like strings. Here we assume valid integer representation is required strictly per the task description "non-integer inputs".
        raise TypeError(f"Input '{stripped_str}' contains invalid number characters.") from e

def check_equality(num1_str, num2_str):
    """
    Checks if two numerical values represented by strings are equal.
    
    Args:
        num1_str (str): First string representation of a number.
        num2_str (str): Second string representation of a number.
        
    Returns:
        bool: True if both inputs successfully parse to the same integer, False otherwise.
                
    Raises:
        TypeError or ValueError: If either input cannot be parsed as an integer and does not meet strict criteria.
    """
    try:
        val1 = safe_parse_integer(num1_str)
    except (ValueError, TypeError):
        return None  # Indicates a parsing error occurred
        
    if num2_str != '' and isinstance(num2_str, str):
        try:
            val2 = safe_parse_integer(num2_str)
        except ValueError as e:
             raise type(e)(f"Second input '{num2_str}' is invalid.") from e

    return val1 == val2

if __name__ == '__main__':
    # Hard-coded sample values to run without user interaction.
    sample_inputs = [350, 946]
    
    result_string = "Equal" if check_equality(str(sample_inputs[0]), str(sample_inputs[1])) else "Not Equal"
    print(result_string)