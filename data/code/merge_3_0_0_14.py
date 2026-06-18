"""
Script to convert a length from meters to feet.

This module provides functionality to convert lengths measured in meters 
to their equivalent value in feet using the standard conversion factor.
The conversion rate is approximately 1 meter = 3.28084 feet.
"""

def meters_to_feet(meters: float) -> float:
    """
    Convert a length from meters to feet.

    Args:
        meters (float): The length in meters to be converted.

    Returns:
        float: The equivalent length in feet.

    Example:
        >>> meters_to_feets(10)
        32.8084
    """
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No interactive input is used as per task requirements.
    
    sample_meters_1 = 5.0
    sample_meters_2 = 10.5
    
    feet_result_1 = meters_to_feet(sample_meters_1)
    print(f"{sample_meters_1} meters is equal to {feet_result_1:.4f} feet.")
    
    feet_result_2 = meters_to_feet(sample_meters_2)
    print(f"{sample_meters_2} meters is equal to {feet_result_2:.4f} feet.")