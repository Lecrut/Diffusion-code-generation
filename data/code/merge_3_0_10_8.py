import math

def meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to feet using the standard conversion factor.
    
    Parameters:
        meters (float): The length value in meters.
        
    Returns:
        float: The equivalent length in feet, rounded to 6 decimal places for precision.
    """
    # Standard conversion factor: 1 meter = 3.28084 feet approximately
    FEET_PER_METER = 3.28084
    
    result = meters * FEET_PER_METER
    return round(result, 6)

if __name__ == '__main__':
    # Hard-coded sample values for testing as per task requirements
    SAMPLE_METERS = [10.5, -5.0, 3280.84]
    
    print("Sample Conversion Test Results:")
    print("-" * 30)
    
    for meters in SAMPLE_METERS:
        try:
            feet = meters_to_feet(meters)
            # Format output to show reasonable precision (e.g., removing trailing zeros if exact integer-like)
            formatted_output = f"{feets:.2f}" if isinstance(feets, float) else str(int(feets))
            
            print(f"Meters: {meters:>10.4} | Feet: {formatted_output}")
        except Exception as e:
            # Graceful error handling for unexpected issues in sample data (unlikely here but demonstrates practice)
            print(f"Error processing value {meters}: {e}")