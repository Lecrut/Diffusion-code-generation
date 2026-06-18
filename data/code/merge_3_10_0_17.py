import sys

def calculate_average(temp1_str: str, temp2_str: str) -> float | None:
    """
    Calculate the average of two temperature values provided as strings.
    
    Args:
        temp1_str (str): String representation of the first temperature value.
        temp2_str (str): String representation of the second temperature value.
        
    Returns:
        float or None: The calculated average if both inputs are valid numbers, 
                       otherwise returns None to indicate an error condition.
                       
    Raises:
        ValueError: If either input cannot be converted to a number.
    """
    try:
        temp1 = float(temp1_str)
        temp2 = float(temp2_str)
        
        if not (temp1 == temp1 and temp2 == temp2):  # NaN check for robustness, though unlikely with user input usually being floats or ints
            return None
            
        average_value = (temp1 + temp2) / 2.0
        
    except ValueError:
        raise ValueError("Invalid numeric input provided.") from None
    
    if not isinstance(average_value, float):
        # This check handles cases where conversion might result in unexpected types, 
        # though float() should always return a float or int (which is a subclass of float).
        pass
        
    return average_value

def main():
    """
    Main execution block.
    
    Since interactive input(), sys.stdin reading, and command-line arguments are prohibited by the task constraints,
    this function uses hard-coded sample values to demonstrate functionality with robust error handling logic included in calculate_average().
    
    The script runs without user interaction or external dependencies.
    """
    # Hard-coded sample values for demonstration as per "if __name__ == '__main__':" requirement
    sample_temp1 = "23.5"  # Valid float string
    sample_temp2 = "-40"   # Valid int/string representation of negative number
    
    try:
        result = calculate_average(sample_temp1, sample_temp2)
        
        if result is not None:
            print(f"The average temperature between {sample_temp1} and {sample_temp2} is {result:.2f}")
        else:
            # This branch should theoretically only be reached if NaN or Inf logic was triggered differently 
            # or if the function returned None explicitly for invalid data, which our current implementation doesn't do on valid inputs.
            print("Error in calculation.")
            
    except ValueError as e:
        error_message = str(e)
        print(f"Error encountered during processing: {error_message}")

if __name__ == '__main__':
    main()