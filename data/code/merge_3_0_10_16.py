import math

def meters_to_feet(meters: float) -> float:
    """
    Converts a length from meters to feet using the standard conversion factor.
    
    The formula used is: feet = meters * 3.28084
    
    Args:
        meters (float): The length in meters.
        
    Returns:
        float: The equivalent length in feet, rounded to two decimal places.
    """
    if not isinstance(meters, (int, float)):
        raise ValueError("Input must be a numeric value.")
    
    conversion_factor = 3.28084
    return round(meters * conversion_factor, 2)

if __name__ == '__main__':
    # Sample values for testing without interactive input
    sample_meters_values = [1, 5.5, -2]

    print("Converting meters to feet...")
    
    for meters in sample_meters_values:
        try:
            feet = meters_to_feet(meters)
            result_string = f"{meters} meters is equal to {feet} feet"
            print(result_string)
        except ValueError as ve:
            print(f"Error processing input '{meters}': {ve}")