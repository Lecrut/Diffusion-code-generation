import math

# Conversion factors to meters (base unit)
TO_METERS = {
    'm': 1,
    'km': 1000,
    'mi': 1609.344,
    'ft': 0.3048,
    'yd': 0.9144,
}

def convert_distance(distance: float, unit_str: str) -> dict[str, float]:
    """
    Converts a given distance in the specified unit to all other supported units.
    
    Args:
        distance (float): The numerical value of the distance.
        unit_str (str): The string representation of the input unit ('m', 'km', 'mi').
        
    Returns:
        dict[str, float]: A dictionary mapping each supported unit to its equivalent 
                          distance in meters first converted from the input.
                          
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be a number.")
    
    valid_units = set(TO_METERS.keys())
    if unit_str.lower() not in valid_units:
        raise ValueError(f"Unsupported unit '{unit_str}'. Supported units are {valid_units}")

    # Convert input to meters, then back to all other units for consistency and efficiency
    base_meters = distance * TO_METERS[unit_str.lower()]
    
    result = {}
    for target_unit in valid_units:
        if target_unit != unit_str.lower():
            converted_value = base_meters / TO_METERS[target_unit]
            # Round to 6 decimal places to avoid floating point noise unless it's an integer case
            rounded_val = round(converted_value, 6)
            
            # Special handling for exact integers if the result is very close
            if abs(rounded_val - int(rounded_val)) < 1e-9:
                final_val = int(rounded_val)
            else:
                final_val = rounded_val
            
            result[target_unit] = final_val

    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    samples = [
        {'distance': 1, 'unit': 'm'},      # Base case: meters
        {'distance': 500, 'unit': 'km'},   # Kilometers
        {'distance': 3.28, 'unit': 'mi'},  # Miles (approx length of a football field)
    ]

    for sample in samples:
        d = sample['distance']
        u = sample['unit']
        
        print(f"Input: {d} {u}")
        converted_units = convert_distance(d, u)
        
        # Print results excluding the input unit itself to show "all other supported units" clearly
        for out_unit in sorted(converted_units.keys()):
            if out_unit != u.lower():
                print(f"{out_unit}: {converted_units[out_unit]}")
                
        print("-" * 30)