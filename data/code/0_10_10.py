def meters_to_feet(meters: float) -> None:
    """
    Converts a given length from meters to feet.
    
    Parameters:
        meters (float): The length in meters to convert.
        
    Returns:
        None
    
    Logic:
        Uses the conversion factor 1 meter = 3.28084 feet.
        Prints the result formatted to two decimal places.
    """
    # Conversion constant defined for precision, though Python handles float arithmetic well enough here.
    METERS_TO_FEET_FACTOR = 3.28084
    
    try:
        if meters < 0:
            print(f"Error: Length cannot be negative.")
            return

        feet_value = meters * METERS_TO_FEET_FACTOR
        
        # Output the result in a readable format
        print(f"{meters} meters is equal to {feet_value:.2f} feet.")
    except TypeError as e:
        print(f"Input error: Cannot convert input of type '{type(meters).__name__}' to float. Please provide a number.")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes, avoiding interactive prompts.
    
    # Sample Case 1: Standard conversion
    meters_sample_1 = 5
    
    # Sample Case 2: Larger distance (e.g., marathon length approx)
    meters_sample_2 = 42195
    
    # Note: No actual input() call is used to ensure the script runs immediately upon execution.

    print("--- Converting sample values ---")
    
    meters_to_feet(meters_sample_1)
    meters_to_feet(meters_sample_2)