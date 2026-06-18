def convert_length(length: float, unit_type: str) -> float:
    """
    Converts a length from various units to meters.

    Supported input units (case-insensitive):
        'm'   - Meters
        'km'  - Kilometers
        'ft'  - Feet
        'in'  - Inches
    
    The function returns the equivalent value in meters as a float.
    
    Args:
        length (float): The numerical value of the length.
        unit_type (str): The string identifier for the source unit ('m', 'km', 'ft', or 'in').

    Returns:
        float: The converted length in meters.

    Raises:
        ValueError: If an unsupported unit type is provided.
    """
    conversion_factors = {
        'm': 1,      # Meters to meters
        'km': 1000,  # Kilometers to meters (multiplier)
        'ft': 0.3048, # Feet to meters
        'in': 0.0254, # Inches to meters
    }

    normalized_unit = unit_type.lower()

    if normalized_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit type '{unit_type}'. Supported units are m, km, ft, in.")

    return length * conversion_factors[normalized_unit]

if __name__ == '__main__':
    pass
