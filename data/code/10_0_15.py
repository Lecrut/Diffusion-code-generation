def calculate_average_temperature(temp1: float, temp2: float) -> float:
    """
    Calculate the average of two temperature values.
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        float: The average of the two temperatures.
    """
    return (temp1 + temp2) / 2

def validate_numeric_input(user_value_str: str, label: str = "Temperature") -> float:
    """
    Validate and convert user input to a numeric value with error handling.
    
    Args:
        user_value_str (str): The string provided by the user.
        label (str): A descriptive name for the variable (e.g., 'First Temperature', 'Second Temperature').
        
    Returns:
        float: The validated floating-point number.
        
    Raises:
        ValueError: If the input cannot be converted to a valid numeric type or is empty.
        TypeError: If an incorrect type of object is passed instead of a string.
    """
    if not isinstance(user_value_str, str):
        raise TypeError(f"{label} must be provided as a string.")

    stripped_input = user_value_str.strip()
    
    try:
        numeric_value = float(stripped_input)
    except ValueError:
        # Attempt to catch non-numeric characters and re-raise with clear message
        if len(stripped_input) == 0:
            raise ValueError(f"{label} cannot be calculated from an empty input.")
            
        try:
            int_value = int(float(stripped_input))
        except (ValueError, OverflowError):
            # If it's not a valid float representation after stripping non-numeric chars or conversion failure
            raise ValueError(f"Invalid value for {label}: '{stripped_input}' cannot be converted to a number.")

    return numeric_value

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no interactive input)
    SAMPLE_TEMP1 = 25.0
    SAMPLE_TEMP2 = 30.0
    
    print(f"Computing average of {SAMPLE_TEMP1}°C and {SAMPLE_TEMP2}°C...")
    
    try:
        # Perform calculation with hard-coded values directly to bypass input() requirement while maintaining logic integrity
        avg_temp = calculate_average_temperature(SAMPLE_TEMP1, SAMPLE_TEMP2)
        
        print(f"The average temperature is: {avg_temp:.2f}°C")
        
    except TypeError as te:
        print(f"Type Error in calculation: {te}")
    
    # Simulating error handling for non-numeric input conceptually within the main block logic if inputs were dynamic, 
    # but since they are hard-coded here, we simply verify the function would handle them correctly via unit testing or by 
    # demonstrating validation on a string that looks like an int to show robustness.
    
    # Demonstration of error handling capability without using input()
    INVALID_INPUT = "abc"  # This is not numeric
    
    print("\n--- Demonstrating Error Handling ---")
    try:
        invalid_temp = validate_numeric_input(INVALID_INPUT, label="Invalid Input Check")
        print(f"This should have failed but got {invalid_temp}")
    except (ValueError, TypeError) as ve:
        # This block executes to show the script handles bad data gracefully without crashing or blocking on input()
        error_msg = f"Caught expected error for invalid numeric string '{INVALID_INPUT}': {ve}"
        print(error_msg)