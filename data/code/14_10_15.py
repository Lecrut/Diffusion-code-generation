"""
Volume Difference Calculator Module

This script calculates the difference between two volume measurements provided by the user.
It includes robust error handling to manage non-numeric inputs gracefully.

The main execution block uses hard-coded sample values and does not rely on any 
interactive input, command-line arguments, or external files/network access.
"""

def parse_numeric_input(value: str) -> float | None:
    """
    Attempts to convert a string value into a floating-point number.
    
    Args:
        value (str): The input string representing the volume measurement.
        
    Returns:
        float or None: The converted numeric value if successful; otherwise, returns None.
    """
    try:
        return float(value)
    except ValueError as e:
        # Silently ignore non-numeric conversions since we want to proceed with samples only in the main block
        print(f"Warning: '{value}' is not a valid number. Conversion failed.")
        raise

def calculate_difference(vol_a: str, vol_b: str) -> float:
    """
    Calculates the absolute difference between two volume measurements after parsing them as floats.
    
    Args:
        vol_a (str): The first volume measurement string.
        vol_b (str): The second volume measurement string.
        
    Returns:
        float: The absolute difference between vol_a and vol_b.
    """
    parsed_vol_a = parse_numeric_input(vol_a)
    
    if parsed_vol_a is None:
        raise ValueError("Error parsing first input.")

    try:
        parsed_vol_b = parse_numeric_input(vol_b)
        
        if parsed_vol_b is None:
            raise ValueError("Error parsing second input.")
            
        diff = abs(parsed_vol_a - parsed_vol_b)
        return float(f"{diff:.2f}")  # Round to two decimal places for cleaner output
        
    except (ValueError, TypeError):
        print("An error occurred while calculating the difference between volumes.")
        raise

if __name__ == '__main__':
    """
    Main execution block with hard-coded sample values.
    
    This section runs without any user input or external dependencies.
    It simulates a scenario where two volume measurements are provided directly in code.
    Sample Input 1: "50" (representing 50 liters)
    Sample Input 2: "75" (representing 75 liters)
    
    Expected Output: The absolute difference is calculated and printed as '25.0'.
    """

    # Hard-coded sample volume measurements
    input_vol_1 = "50"
    input_vol_2 = "75"

    try:
        result_difference = calculate_difference(input_vol_1, input_vol_2)
        
        print("Calculation completed successfully.")
        print(f"Difference between {input_vol_1} and {input_vol_2}: {result_difference}")
        
    except ValueError as ve:
        # This block catches any errors from the calculation function (like non-numeric simulation if we changed inputs)
        print("\nFinal Error Status:", str(ve))