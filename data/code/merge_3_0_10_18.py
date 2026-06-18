"""
Script to convert a length from meters to feet.

This module defines functions to handle unit conversion between metric (meters) 
and imperial/US customary units (feet). It includes input validation and error handling 
to ensure robust execution even with invalid user inputs.

Conversion factor: 1 meter = approximately 3.28084 feet.
"""

def meters_to_feet(meters):
    """
    Convert a length from meters to feet.

    Args:
        meters (float or int): The length in meters. Must be non-negative.

    Returns:
        float: The equivalent length in feet, rounded to 4 decimal places for clarity.

    Raises:
        ValueError: If the input is not a number or if it represents negative values.
    """
    try:
        # Attempt to convert input to float first to handle integer inputs as well
        value = float(meters)
        
        if value < 0:
            raise ValueError("Length cannot be negative.")
            
        conversion_factor = 3.28084
        feet_value = value * conversion_factor
        
        return round(feet_value, 4)
    except (ValueError, TypeError):
        # This block catches cases where input is not a valid number or type
        raise ValueError("Input must be a non-negative numeric value.")

def main():
    """
    Main execution function.

    Although the task requires user interaction in general logic, 
    this specific requirement mandates that sample values are used within 
    an 'if __name__ == "__main__":' block without interactive prompts for testing purposes.
    
    The script demonstrates usage with hard-coded samples and prints results to console.
    """
    # Sample input 1: Valid positive integer
    sample_input_1 = "5"
    
    # Sample input 2: Valid float string
    sample_input_2 = "3.5"
    
    # Simulate user interaction for demonstration without actual blocking prompts
    
    print("--- Conversion Demo ---")
    
    try:
        meters_val = int(sample_input_1) if '.' not in sample_input_1 else float(sample_input_1)
        feet_result = meters_to_feet(meters_val)
        print(f"{meters_val} meters is equal to {feet_result} feet.")

    except ValueError as ve:
        # Handle potential conversion errors from the string parsing or logic inside function
        if "negative" in str(ve).lower():
            print("Error:", ve)
        else:
            print(f"Input Error for sample 1: {ve}")

    
    try:
        meters_val = float(sample_input_2)
        feet_result = meters_to_feet(meters_val)
        print(f"{meters_val} meters is equal to {feet_result} feet.")
        
    except ValueError as ve:
        if "negative" in str(ve).lower():
            print("Error:", ve)
        else:
            # Example of handling a non-numeric string passed directly (simulating bad input logic flow)
            # In a real interactive scenario, this would be caught by the user prompt loop.
            pass

if __name__ == '__main__':
    main()