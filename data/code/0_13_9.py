import sys

def parse_length_measurements(input_str: str) -> list[float]:
    """
    Parses a string of length measurements separated by spaces into a list of floats.
    
    Args:
        input_str (str): A space-separated string representing numerical values in kilometers.
        
    Returns:
        list[float]: List of float values representing lengths in kilometers.
    """
    try:
        return [float(x.strip()) for x in input_str.split()] if input_str else []
    except ValueError as e:
        raise ValueError(f"Invalid numeric value provided: {e}")

def convert_to_meters(kilometers: float) -> float:
    """Converts kilometers to meters."""
    return kilometers * 1000.0

def convert_to_feet(meters: float) -> float:
    """Converts meters to feet using the standard conversion factor (1 meter = 3.28084 feet)."""
    return meters * 3.28084

if __name__ == '__main__':
    # Hard-coded sample values in kilometers as per task requirement, no interactive input used here.
    SAMPLE_VALUES_KM = "15.7 20.0 25.5"

    try:
        measurements_km = parse_length_measurements(SAMPLE_VALUES_KM)
        
        for km_value in measurements_km:
            meters_val = convert_to_meters(km_value)
            feet_val = convert_to_feet(meters_val)
            
            # Output formatted string showing original value, equivalent in meters and feet.
            print(f"{km_value} kilometers is equal to {meters_val:.2f} meters or approximately {feet_val:.2f} feet.")
    except ValueError as e:
        sys.stderr.write(f"Error processing input: {e}\n")