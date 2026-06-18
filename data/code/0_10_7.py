"""
Module to convert length from meters to feet.

This script provides a function to perform the conversion using the standard factor 
(1 meter = 3.28084 feet) and includes an example usage block with hard-coded values.
Conversion errors due to invalid input types are handled within the main execution flow, 
though the primary conversion logic assumes valid numeric arguments.

Conversion formula: feet = meters * 3.28084
"""

def convert_meters_to_feet(meters):
    """
    Converts a length value from meters to feet.

    Args:
        meters (float or int): The length in meters to be converted.

    Returns:
        float: The equivalent length in feet, rounded to 4 decimal places for standard precision.
    
    Raises:
        TypeError: If the input is not a numeric type.
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be an integer or a float.")

    conversion_factor = 3.28084
    feet_value = meters * conversion_factor
    
    return round(feet_value, 4)

def main():
    """
    Main function demonstrating the convert_meters_to_feet utility 
    with hard-coded sample values as requested.
    
    This block does not perform interactive input but illustrates how the module works.
    It includes error handling for invalid inputs in a simulated scenario to demonstrate robustness.
    """

    # Sample valid test case 1: Convert 5 meters to feet
    print("Sample Test Case 1:")
    sample_meters_1 = 5.0
    try:
        result_feet_1 = convert_meters_to_feet(sample_meters_1)
        print(f"{sample_meters_1} meters is equal to {result_feet_1} feet.")
    except TypeError as e:
        print(f"Error in Test Case 1: {e}")

    # Sample valid test case 2: Convert an integer (10) meters to feet
    print("\nSample Test Case 2:")
    sample_meters_2 = 10
    try:
        result_feet_2 = convert_meters_to_feet(sample_meters_2)
        print(f"{sample_meters_2} meters is equal to {result_feet_2} feet.")
    except TypeError as e:
        print(f"Error in Test Case 2: {e}")

    # Sample error handling test case: Attempting to convert non-numeric input (handled gracefully)
    print("\nSample Error Handling Test:")
    invalid_input = "ten" 
    try:
        result_feet_invalid = convert_meters_to_feet(invalid_input)
        print(f"{invalid_input} meters is equal to {result_feet_invalid} feet.")
    except TypeError as e:
        print(f"Caught expected error for non-numeric input '{invalid_input}':")
        print(e)

if __name__ == '__main__':
    # Execute the main logic when this script is run directly.
    main()