import sys

# Define conversion factors to meters (SI unit)
TO_METERS = {
    'm': 1,      # meters
    'km': 0.001, # kilometers
    'cm': 100,   # centimeters
    'mm': 1000,  # millimeters
    'mi': 160934.4, # miles (US)
    'yd': 0.9144, # yards
    'ft': 0.3048, # feet
    'nmi': 1852,   # nautical miles
}

# Define meters to conversion factors for target units
FROM_METERS = {value: key for key, value in TO_METERS.items()}

def convert_distance(distance_value: float, from_unit: str, to_unit: str) -> tuple[float, list[str]]:
    """
    Converts a distance between any supported unit pair.
    
    Args:
        distance_value (float): The numerical value of the distance.
        from_unit (str): Source unit abbreviation ('m', 'km', etc.).
        to_unit (str): Target unit abbreviation ('m', 'mi', etc.).
        
    Returns:
        tuple[float, list[str]]: 
            - Converted float value in target units.
            - List of error messages if conversion fails.
            
    Raises/Returns Errors for invalid inputs or unsupported units.
    """
    
    errors = []

    # Check if source unit is supported
    if from_unit not in TO_METERS:
        errors.append(f"Error: Unsupported input unit '{from_unit}'. Supported units are: {', '.join(TO_METERS.keys())}.")
        
    else: 
        meters = distance_value * TO_METERS[from_unit]

    # Check if target unit is supported
    if to_unit not in FROM_METERS:
        errors.append(f"Error: Unsupported output unit '{to_unit}'. Supported units are: {', '.join(FROM_METERS.keys())}.")
        
    else: 
        converted_value = meters / FROM_METERS[to_unit]

    return (converted_value, [])

def format_output(value: float) -> str:
    """
    Formats the numerical value for better readability.
    
    Args:
        value (float): The calculated distance in target units.
        
    Returns:
        str: Formatted string of the result with appropriate unit abbreviation.
    """
    abbreviations = TO_METERS.keys()

    # Find the key corresponding to current meters conversion factor logic isn't needed here, just use direct lookup on FROM_METERS or generic mapping?
    # Actually, we need the target unit's full name if possible, but we don't have names. 
    # Let's stick to standard abbreviations as per task simplicity unless specific naming is requested.
    
    return f"{value:.6f} {abbreviations[-1]}"

def get_unit_name(unit_key: str) -> str:
    """Returns a descriptive name for the unit key."""
    names = {
        'm': "meter",
        'km': "kilometer",
        'cm': "centimeter",
        'mm': "millimeter",
        'mi': "mile (US)",
        'yd': "yard",
        'ft': "foot",
        'nmi': "nautical mile"
    }
    return names.get(unit_key, unit_key)

if __name__ == '__main__':
    pass
