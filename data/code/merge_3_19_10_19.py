import re

def validate_integer_input(input_string: str) -> int | None:
    """
    Validates if a string represents an integer.
    
    Args:
        input_string (str): The string to check.
        
    Returns:
        int or None: The parsed integer if valid, None otherwise.
    """
    # Regex pattern for optional sign followed by digits
    pattern = r'^[-+]?[0-9]+$'
    
    if not isinstance(input_string, str):
        return None
        
    match = re.match(pattern, input_string.strip())
    if match:
        try:
            return int(match.group(0))
        except ValueError:
            # Fallback for extremely large numbers that might overflow standard conversions in some environments, 
            # though Python handles arbitrary precision integers. This block is defensive.
            pass
            
    return None

def compare_numbers(num1_str: str | None = None, num2_str: str | None = None) -> bool:
    """
    Compares two numbers after validating their input strings.
    
    Args:
        num1_str (str or None): String representation of the first number. Defaults to None.
        num2_str (str or None): String representation of the second number. Defaults to None.
        
    Returns:
        bool: True if the first number is strictly greater than the second, False otherwise.
              Raises ValueError if inputs are invalid integers.
    """
    # Default sample values for standalone execution without user input
    default_num1 = "42"
    default_num2 = "30"

    num1_str_to_use = num1_str if num1_str is not None else default_num1
    num2_str_to_use = num2_str if num2_str is not None else default_num2
    
    # Validate inputs and parse integers
    def get_int(value: str) -> int | None:
        return validate_integer_input(value)

    parsed_num1 = get_int(num1_str_to_use)
    parsed_num2 = get_int(num2_str_to_use)

    if parsed_num1 is None or parsed_num2 is None:
        raise ValueError("Input strings must be valid integers.")

    # Perform comparison using Python's arbitrary precision integer support
    return parsed_num1 > parsed_num2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no args)
    SAMPLE_NUM_1 = "42"
    SAMPLE_NUM_2 = "30"

    try:
        result = compare_numbers(SAMPLE_NUM_1, SAMPLE_NUM_2)
        
        if result:
            print(f"The number {SAMPLE_NUM_1} is strictly greater than {SAMPLE_NUM_2}.")
        else:
            print(f"{SAMPLE_NUM_1} is not strictly greater than {SAMPLE_NUM_2}.")

    except ValueError as e:
        print(f"Error during comparison: {e}")