import math

# Conversion factors to meters (base unit)
TO_METERS = {
    'm': 1,
    'km': 1000,
    'mi': 1609.344,
    'ft': 0.3048,
    'yd': 0.9144,
    'cm': 0.01,
}

def convert_distance(value: float, unit_str: str) -> dict[str, float]:
    """
    Converts a given distance value from the specified unit to all other supported units.
    
    Args:
        value (float): The numeric distance value.
        unit_str (str): String representing the source unit ('m', 'km', 'mi').
        
    Returns:
        dict[str, float]: A dictionary mapping each target unit string to its equivalent 
                         converted distance in meters first, then scaled appropriately.
    
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number.")
        
    source_unit = unit_str.lower()
    
    # Validate input units against supported set
    valid_units = list(TO_METERS.keys())
    if source_unit not in TO_METERS:
        raise ValueError(f"Unsupported unit '{source_unit}'. Supported units are {valid_units}.")

    # Convert to meters first using the most efficient single multiplication/division operation
    value_in_meters = value * TO_METERS[source_unit]
    
    result = {}
    for target_unit, factor in TO_METERS.items():
        if target_unit == source_unit:
            result[target_unit] = round(value)  # Return original integer-like input as is if possible
        else:
            converted_value = value_in_meters / factor
            # Round to reasonable precision based on typical distance measurements (6 decimal places for meters, less for larger units usually not needed but safe here)
            result[target_unit] = round(converted_value, 9)

    return result

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    
    samples = [
        {'value': 10.5, 'unit': 'm'},
        {'value': 2.34, 'unit': 'km'},
        {'value': 5, 'unit': 'mi'},
        {'value': 1609.344, 'unit': 'ft'} # Testing with a unit that is not in the initial TO_METERS list above to ensure error handling works if we added it later, but currently only m/km/mi are strictly requested as examples. 
    ]
    
    # Note: The prompt specifically asked for 'm', 'km', 'mi' as examples. I will add support for others in the logic (ft/yd/cm) to make "all other supported units" meaningful, but ensure samples use m/km/mi primarily or valid ones if added. 
    # Let's stick strictly to the requested example set + a couple derived ones that are mathematically sound conversions from meters.
    
    test_cases = [
        (100, 'km'),
        (5280, 'mi'),  # Exactly one mile in feet? No, let's use standard values. 
                     # Let's just use the requested examples and maybe cm for completeness if it doesn't break "efficient".
    ]

    print("Distance Conversion Results:")
    
    # Sample 1: Meters to all units (m -> km, mi)
    res = convert_distance(500.75, 'm')
    print(f"\nInput: {res['m']} m")
    for unit, val in sorted(res.items()):
        if unit != 'm': # Skip original value display to avoid redundancy or just show all as requested "all other" implies including self usually? 
            # The prompt says "equivalent distance in ALL OTHER supported units". Usually this means the set of conversions. Returning the input back is standard practice unless explicitly excluded.
            print(f"{val} {unit}")

    # Sample 2: Kilometers to all units (km -> m, mi)
    res = convert_distance(10, 'km')
    print(f"\nInput: {res['km']} km")
    for unit, val in sorted(res.items()):
        if unit != 'km':
            print(f"{val} {unit}")

    # Sample 3: Miles to all units (mi -> m, km)
    res = convert_distance(1.5, 'mi')
    print(f"\nInput: {res['mi']} mi")
    for unit, val in sorted(res.items()):
        if unit != 'mi':
            print(f"{val} {unit}")

    # Sample 4: A value that might be tricky with rounding (e.g. exact meter conversion)
    res = convert_distance(160934.4, 'm') # This is exactly 10 miles in meters? No, 5280*1760 = 9257600 ft -> m... 
                                            # Let's just use a clean number like 1 mile converted to km
    res_km = convert_distance(1.0, 'mi')
    print(f"\nInput: {res_km['mi']} mi")
    for unit, val in sorted(res_km.items()):
        if unit != 'mi':
            print(f"{val} {unit}")