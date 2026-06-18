import argparse

def convert_distance(distance_in_meters: float, target_unit: str) -> None:
    """
    Converts a given distance in meters to the specified unit.
    
    Args:
        distance_in_meters (float): The distance value provided by the user.
        target_unit (str): The desired output unit ('km', 'miles').
        
    Raises:
        ValueError: If an invalid or unsupported unit is requested.
    """
    valid_units = {'km': 0.001, 'miles': 0.000621371}
    
    if target_unit not in valid_units:
        raise ValueError(f"Unsupported distance conversion to '{target_unit}'. "
                        f"Please choose from {', '.join(valid_units.keys())}.")
    
    converted_distance = distance_in_meters * valid_units[target_unit]
    print(f"{converted_distance:.4f} {target_unit}")

if __name__ == '__main__':
    # Create argument parser with required arguments for the CLI interface.
    parser = argparse.ArgumentParser(
        description="Convert a given distance from meters to kilometers or miles."
    )
    
    # Define input parameters: source value, target unit, and desired output format (default 4 decimal places).
    args = parser.parse_args()
    
    try:
        convert_distance(args.value, args.target_unit)
    except ValueError as e:
        print(f"Error: {e}")