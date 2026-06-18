import sys

def is_positive(value):
    """Check if a given value is strictly positive."""
    return value > 0

def validate_integer(input_str):
    """Validate that input string represents an integer and convert it to int.
    
    Args:
        input_str (str): The input string provided by the user or sample data.
        
    Returns:
        int: The parsed integer.
        
    Raises:
        ValueError: If the input is not a valid integer representation.
        TypeError: If an expected non-string type is passed to this function.
    """
    try:
        return int(input_str)
    except (ValueError, OverflowError):
        raise ValueError(f"Invalid integer input received: '{input_str}'")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_values = ["42", "-5", "0.7", "", "abc", "+10"]
    
    print("Running automated tests with hard-coded input samples:")
    
    for value_str in test_values:
        try:
            num_value = validate_integer(value_str)
            result = is_positive(num_value)
            status_msg = "Result: Positive" if result else f"Not positive (is {num_value})"
            print(f"Input '{value_str}' -> Number: {num_value} | {status_msg}")
        except ValueError as e:
            # This catches cases where input is not a valid integer string
            # Note: "0.7", "", and "abc" will raise ValueError here
            print(f"Error processing '{value_str}': Non-integer or invalid format.")