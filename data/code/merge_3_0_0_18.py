def convert_meters_to_feet(meters: float) -> float:
    """
    Converts a length from meters to feet using the standard conversion factor (1 meter = 3.28084 feet).
    
    Args:
        meters (float): The length in meters.
        
    Returns:
        float: The equivalent length in feet.
    """
    return meters * 3.28084

if __name__ == '__main__':
    # Sample input values for demonstration purposes without interactive prompts.
    sample_meters = [1, 5, -9]

    print("Meters to Feet Conversion")
    
    for value in sample_meters:
        feet_value = convert_meters_to_feet(value)
        formatted_output = f"{value:.2f} meters is {feet_value:.4f} feet"
        print(formatted_output)