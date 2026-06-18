"""
Module to convert length from meters to feet.

This script defines a function to perform the conversion using the standard factor 
(1 meter = 3.28084 feet) and includes an example usage block in the main section.
"""

def meters_to_feet(meters: float) -> float:
    """
    Convert a length given in meters to its equivalent in feet.

    Args:
        meters (float): The length value in meters.

    Returns:
        float: The converted length in feet.
    
    Example:
        >>> meters_to_feet(1)
        3.28084
    
    Note:
        The conversion factor used is exactly 3.28084 (approximation of 
        the international foot definition relative to the meter).
    """
    feet_per_meter = 3.28084
    return meters * feet_per_meter

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes
    sample_meters_1 = 5.0
    sample_meters_2 = 10.0
    
    result_1 = meters_to_feet(sample_meters_1)
    print(f"{sample_meters_1} meters is equal to {result_1:.4f} feet.")
    
    result_2 = meters_to_feet(sample_meters_2)
    print(f"{sample_meters_2} meters is equal to {result_2:.4f} feet.")