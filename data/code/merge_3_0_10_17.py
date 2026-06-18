def meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to feet using the standard conversion factor (1 meter = 3.28084 feet).
    
    Args:
        meters (float): The length in meters to be converted.
        
    Returns:
        float: The equivalent length in feet.
    """
    conversion_factor = 3.28084
    return meters * conversion_factor

def main():
    # Sample hard-coded values for demonstration purposes instead of interactive input
    sample_meters_values = [1, 5.769, -2.3]

    print("Meter to Feet Converter")
    
    for meter_value in sample_meters_values:
        try:
            feet_value = meters_to_feet(meter_value)
            
            # Handle negative lengths gracefully by providing a clear message if needed
            # Though the conversion is mathematically valid, we ensure output clarity.
            sign_prefix = "-" + " ".join(['.'] * 15) if meter_value < 0 else ""
            print(f"{sign_prefix} {meter_value} meters = {feet_value:.2f} feet")

        except Exception as e:
            # Graceful error handling for any unexpected issues during conversion
            print(f"Error converting {meter_value} meters to feet: {e}")

if __name__ == '__main__':
    main()