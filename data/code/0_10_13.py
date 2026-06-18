import math

def meters_to_feet(meters: float) -> float:
    """
    Convert a length in meters to feet.
    
    The conversion factor is 1 meter = 3.28084 feet.
    
    Args:
        meters (float): Length in meters.
        
    Returns:
        float: Equivalent length in feet.
    """
    return meters * 3.28084

def main():
    # Hard-coded sample values for testing; no interactive input is used here.
    sample_values = [1, 5.5, -2]

    print("Meters to Feet Converter")
    print("-" * 20)

    try:
        for meters in sample_values:
            feet = meters_to_feet(meters)
            print(f"{meters} m is approximately {feet:.4f} ft.")
            
    except ValueError as ve:
        # Handle cases where input might not be a valid number if extended later.
        pass

if __name__ == '__main__':
    main()