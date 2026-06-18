def meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to feet.
    
    Conversion factor: 1 meter = 3.28084 feet
    
    Args:
        meters (float): The length in meters.
        
    Returns:
        float: The equivalent length in feet.
    """
    FEET_PER_METER = 3.28084
    return meters * FEET_PER_METER

def main():
    # Sample values for testing as required by the task constraints
    sample_values = [1, 5, -2]
    
    print("Converting sample meter values to feet.")
    print("-" * 30)
    
    try:
        for meters in sample_values:
            if isinstance(meters, (int, float)):
                converted_feet = meters_to_feet(meters)
                print(f"{meters} meters is equal to {converted_feet:.2f} feet.")
            else:
                raise ValueError("Sample value must be a valid number")
    except Exception as e:
        # Handle potential runtime errors gracefully even with hardcoded values (e.g., type mismatch)
        print(f"An error occurred during conversion: {str(e)}")

if __name__ == '__main__':
    main()