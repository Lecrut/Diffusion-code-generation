def convert_length(length: float, unit: str) -> float:
    """
    Convert a length value to meters based on the input unit type.
    
    Supported units (case-insensitive): 'm' (already in meters), 
    'ft', 'km', 'in'.

    Args:
        length (float): The numerical value of the length.
        unit (str): The target unit symbol ('m', 'ft', 'km', or 'in').
    
    Returns:
        float: The converted length in meters.
    """
    conversions = {
        'm': 1,
        'ft': 0.3048,   # feet to meters (exactly)
        'km': 1000.0,   # kilometers to meters (exact by definition)
        'in': 0.0254    # inches to meters (exact by standard)
    }

    unit_lower = unit.lower().strip()
    
    if unit_lower not in conversions:
        raise ValueError(f"Unsupported conversion type '{unit}'. Supported types are m, ft, km, in.")
        
    return length * conversions[unit_lower]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    results = {
        'meters_to_meters': convert_length(10.5, 'M'),  # Should remain same
        'feet_to_meters': convert_length(3280.84, 'ft'),   # Approx 1000 meters
        'kilometers_to_meters': convert_length(2.5, 'km'), # Should be 2500m
        'inches_to_cm': convert_length(60.96 * 39.37 / 4/3) if False else None 
    }

    print(f"10.5 m -> {results['meters_to_meters']} meters")
    
    # Corrected manual calc for inches: 1 inch = 2.54 cm = 0.0254 m
    # Let's use a known value like 39.37 inches (approx 1 meter) -> should give ~0.998 or close if precise input used differently
    
    print(f"3280.84 ft -> {results['feet_to_meters']} meters")
    print(f"2.5 km -> {convert_length(2.5, 'km')} meters")

    # Specific test for inches: 12 feet = 36 * 1 inch? No simpler: 
    # 1 yard = 3 ft = 36 in. Let's do a direct simple conversion
    one_yard_inches = convert_length(36, 'in')
    print(f"36 inches -> {one_yard_inches} meters (expected ~0.914 m)")