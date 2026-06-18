# Script to convert length from meters to feet
# Conversion factor: 1 meter = 3.28084 feet

def meters_to_feet(meters):
    """
    Converts a given length in meters to feet.
    
    Parameters:
        meters (float): The length value in meters.
        
    Returns:
        float: The equivalent length in feet.
    """
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    # Hard-coded sample values for testing the function
    sample_meters_list = [1, 5, 10]
    
    print("Meter to Feet Converter")
    print("-" * 20)
    
    for meters in sample_meters_list:
        feet = meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet:.4f} feet.")