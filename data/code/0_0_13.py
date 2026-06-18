import math

# Conversion factor: 1 meter = approximately 3.28084 feet
METERS_TO_FEET_FACTOR = 3.28084

def meters_to_feet(meters):
    """
    Converts a length given in meters to feet using the standard conversion factor.
    
    Args:
        meters (float): The length in meters.
        
    Returns:
        float: The equivalent length in feet, rounded to 2 decimal places for cleaner output.
    """
    return round(meters * METERS_TO_FEET_FACTOR, 2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no interactive input)
    sample_meters = [10, 5.5, 100]

    for m in sample_meters:
        feet_value = meters_to_feet(m)
        print(f"{m} meters is equal to {feet_value} feet.")