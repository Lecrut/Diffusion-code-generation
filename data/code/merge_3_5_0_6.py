def calculate_difference(value1: float | int, value2: float | int) -> tuple[float | None, str]:
    """
    Calculates the difference between two length measurements.
    
    Args:
        value1 (float|int): The first measurement.
        value2 (float|int): The second measurement.
        
    Returns:
        tuple[None|float, str]: A tuple containing either the result or None with an error message, 
                               and always includes a status string indicating success or failure.
    
    Raises:
        TypeError: If inputs are not numeric.
    """
    try:
        # Validate input types to ensure they are numbers
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            result = value1 - value2
            return result, "Success"
        else:
            raise TypeError("Both arguments must be numeric values.")
    except Exception as e:
        # Handle any unexpected exceptions during calculation
        return None, f"Error: {str(e)}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    length_a = 10.5
    length_b = 4.2
    
    diff_message = calculate_difference(length_a, length_b)
    
    if isinstance(diff_message[0], (int, float)):
        print(f"Difference: {diff_message[0]}")
        status = "Success"
    else:
        print("Operation failed.")
        status = diff_message[1]  # This will be the error message string
    
    print(f"Status: {status}")

# Additional test case for non-numeric input without interactive prompts
def test_error_handling():
    try:
        invalid_input = "invalid_string"
        result, msg = calculate_difference(5.0, invalid_input)
        
        if not isinstance(result, (int, float)):
            print("Test passed correctly identified error for non-numeric input.")
            print(f"Error message received: {msg}")
    except Exception as e:
        # The function itself handles the exception internally and returns None/error string
        pass

# Running additional test if executed in this context to demonstrate robustness without args
if __name__ == '__main__':
    # Re-declaring main block logic for clarity within single file execution scope 
    # or simply running the specific validation as a demonstration of capability.
    
    print("--- Test Case 2: Non-numeric Input ---")
    result, msg = calculate_difference(50, "not_a_number")
    if not isinstance(result, (int, float)):
        print("Handled non-numeric input gracefully.")
        print(f"Message: {msg}")

# Note on structure: The script defines the function and includes two main execution blocks 
# within the __main__ scope to demonstrate both successful calculation and error handling.