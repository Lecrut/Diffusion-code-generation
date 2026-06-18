import math

def convert_distance(distance: float, unit: str) -> dict:
    """
    Converts a given distance into all supported units using efficient mathematical operations.
    
    Supported units (abbreviations): 'm' (meter), 'km' (kilometer), 'mi' (mile).
    
    Args:
        distance (float): The numerical value of the distance.
        unit (str): The string abbreviation for the input unit ('m', 'km', or 'mi').
        
    Returns:
        dict: A dictionary mapping each supported unit to its equivalent float value.
            
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    
    # Define conversion factors relative to meters (base unit)
    # 1 meter = 1 m, 0.001 km, ~5.629e-4 mi
    # 1 kilometer = 1000 m, 1 km, ~0.621371 mi
    # 1 mile = ~1609.344 m, ~0.000621371 km, 1 mi
    
    factors_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344 # International mile definition is exact: 5280 * 1.609344 yards where yard=0.9144m exactly
    }
    
    if unit not in factors_to_meters:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are 'm', 'km', and 'mi'.")

    # Convert input distance to meters first (most efficient single conversion)
    value_in_meters = distance * factors_to_meters[unit]
    
    result = {}
    for u in ['m', 'km', 'mi']:
        if u == unit:
            result[u] = round(value_in_meters / factors_to_meters[u], 6) # Round to avoid floating point noise on original input representation logic, though exact division should yield clean numbers usually. Actually, let's keep precision high but rounded for display consistency without losing meaningful data. Standard float repr is often sufficient, but rounding helps with the "efficient" look of normalized output if desired. However, strict math efficiency implies minimal ops. Let's just return calculated values.
        else:
            result[u] = round(value_in_meters / factors_to_meters[u], 6)

    # Re-evaluating rounding strategy for maximum utility without unnecessary loss: 
    # The prompt asks for "equivalent distance". Floating point precision is inherent to the math operation. 
    # Rounding makes it readable and consistent across different inputs (e.g., inputting a rounded km value).
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values running without user input, CLI args, or network access
    
    samples = [
        ('m', 10),           # Input: 10 meters -> Output dict with m, km, mi
        ('km', 2.5),         # Input: 2.5 kilometers 
        ('mi', 3)            # Input: 3 miles
    ]

    for input_unit, distance in samples:
        converted = convert_distance(distance, input_unit)
        print(f"Input: {distance} {input_unit}")
        print("Converted values:")
        for u, val in converted.items():
            print(f"{u}: {val}")
        print("-" * 20)