"""
Script to check if two numbers entered by a user (or sample values) are equal.
This version includes hard-coded sample execution as per requirements, avoiding any interactive input prompts.
"""

def parse_number(input_string):
    """
    Attempts to convert an input string to an integer.
    
    Args:
        input_string (str): The string representation of a number.
        
    Returns:
        int: The parsed integer value if successful.
        
    Raises:
        ValueError: If the string cannot be converted to an integer.
    """
    try:
        return int(input_string)
    except ValueError as e:
        raise ValueError(f"Invalid input '{input_string}': {e}")

def are_numbers_equal(num1_str, num2_str):
    """
    Checks if two string inputs represent equal numerical values.
    
    Args:
        num1_str (str): String representation of the first number.
        num2_str (str): String representation of the second number.
        
    Returns:
        bool: True if both strings parse to the same integer, False otherwise.
    """
    try:
        value1 = parse_number(num1_str)
        value2 = parse_number(num2_str)
        return value1 == value2
    except ValueError as e:
        print(f"Error processing inputs: {e}")
        return None

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction.
    sample_input_1 = "42"
    sample_input_2 = "43"

    result = are_numbers_equal(sample_input_1, sample_input_2)

    if result is None:
        print("One or both inputs were invalid.")
    elif result:
        print(f"The numbers {sample_input_1} and {sample_input_2} are equal.")
    else:
        print(f"The numbers {sample_input_1} and {sample_input_2} are not equal.")

# Additional test case with a valid match for verification logic.
test_case_match = ("5", "05")  # Note: int("05") is 5, so they should be equal.
result_test = are_numbers_equal(*test_case_match)
if result_test:
    print(f"Test passed: {test_case_match[0]} and {test_case_match[1]} are numerically equal.")

# Test case with invalid input to demonstrate error handling in the function logic (though not triggered here).
invalid_input = ("abc", "42")
result_invalid = are_numbers_equal(*invalid_input)
if result_invalid is None:
    print("Error handling works correctly for non-integer inputs.")