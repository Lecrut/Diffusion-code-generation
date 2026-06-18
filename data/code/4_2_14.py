import math

# Conversion factors relative to meters (1 unit = factor * meter)
UNIT_FACTORS = {
    'm': 1,           # meters
    'km': 0.001,      # kilometers
    'mi': 0.000621371, # miles
    'ft': 0.0003048,   # feet (exact)
    'yd': 0.0009144,   # yards (exact)
}

def convert_distance(distance: float, unit_str: str) -> dict[str, float]:
    """
    Converts a given distance in the specified unit to all other supported units.
    
    Args:
        distance (float): The numerical value of the distance.
        unit_str (str): The string representing the source unit ('m', 'km', 'mi').
        
    Returns:
        dict[str, float]: A dictionary mapping each unit symbol to its equivalent 
                          distance in meters converted back to that specific unit.
    
    Raises:
        ValueError: If the provided unit_str is not supported.
    """
    if unit_str not in UNIT_FACTORS:
        raise ValueError(f"Unsupported unit '{unit_str}'. Supported units are {list(UNIT_FACTORS.keys())}")

    # Convert input distance to meters first (the base reference)
    value_in_meters = distance * UNIT_FACTORS[unit_str]
    
    result = {}
    for target_unit, factor in UNIT_FACTORS.items():
        if target_unit == unit_str:
            result[target_unit] = round(distance, 6) # Direct return to avoid precision drift issues on same unit
        else:
            value_in_target = value_in_meters / factor
            result[target_unit] = round(value_in_target, 9)

    return result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        {'value': 10.5, 'unit': 'm'},      # Meters to others
        {'value': 2.34, 'unit': 'km'},     # Kilometers to others
        {'value': 5, 'unit': 'mi'},        # Miles to others
    ]

    print("Distance Conversion Results:")
    for case in test_cases:
        d_val = case['value']
        u_str = case['unit']
        
        try:
            conversions = convert_distance(d_val, u_str)
            
            # Print header for this specific input
            print(f"\nInput: {d_val} {u_str}")
            print("Converted to all units:")
            
            # Sort keys for consistent output order (m, ft, km, mi, yd) based on alphabetical or defined list
            sorted_units = sorted(conversions.keys())
            for u in sorted_units:
                val = conversions[u]
                display_val = f"{val:.6f}" if abs(val - round(val)) < 1e-5 else f"{val:.9f}" # Format nicely based on precision needed
                print(f"  {u}: {display_val}")

        except ValueError as e:
            print(f"Error processing input {d_val} in unit {u_str}: {e}")