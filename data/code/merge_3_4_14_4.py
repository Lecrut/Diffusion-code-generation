import argparse

def convert_distance(distance: float, from_unit: str, to_unit: str) -> tuple[float, bool]:
    """
    Converts a distance value between metric units (km, m, cm).
    
    Args:
        distance: The numerical distance value.
        from_unit: Source unit ('km', 'm', or 'cm').
        to_unit: Target unit ('km', 'm', or 'cm').
        
    Returns:
        A tuple containing the converted distance and a boolean indicating success.
    """
    
    # Define conversion factors relative to meters (1 km = 1000 m, 1 cm = 0.01 m)
    unit_factors = {
        'km': 1000,
        'm': 1,
        'cm': 0.01
    }

    # Validate input units against allowed set and convert to meters first
    if from_unit not in unit_factors or to_unit not in unit_factors:
        return distance, False
    
    try:
        value_in_meters = distance * unit_factors[from_unit]
        
        # Convert from meters to target unit
        converted_value = value_in_meters / unit_factors[to_unit]
        return converted_value, True
        
    except (TypeError, ZeroDivisionError):
        return 0.0, False

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Convert distances between metric units.')
    # Define arguments without making them required to satisfy constraints
    
    distance_arg = parser.add_argument(
        'distance', 
        type=float, 
        help='The numerical value of the distance'
    )
    
    from_unit_arg = parser.add_argument(
        '--from-unit', 
        default=None, 
        choices=['km', 'm', 'cm'], 
        help='Source unit (default: km)'
    )
    
    to_unit_arg = parser.add_argument(
        '--to-unit', 
        default=None, 
        choices=['km', 'm', 'cm'], 
        help='Target unit (default: m)'
    )
    
    args = parser.parse_args()

    # Hard-coded sample values for demonstration as per task requirements
    
    if not args.from_unit or not args.to_unit:
        
        distance_sample = 5.0
        
        from_unit_val = 'km' if not args.from_unit else args.from_unit
        to_unit_val = 'm' if not args.to_unit else args.to_unit
        
        converted_value, is_success = convert_distance(distance_sample, from_unit_val, to_unit_val)

        
        print(f"Input: {distance_sample} {from_unit_val}")
        print(f"Output: {converted_value:.4f} {to_unit_val}" if is_success else f"Error: Invalid unit combination")