def convert_length(length: float, unit: str) -> float:
    """
    Converts a length value from one unit to another (meters <-> feet).
    
    Args:
        length (float): The numeric length value.
        unit (str): The current unit ('m' for meters or 'ft' for feet).
        
    Returns:
        float: The converted length in the opposite unit if conversion is needed,
               otherwise returns the original value formatted to avoid floating point noise 
               when units match but logic requires outputting a consistent representation.
    
    Note: This function assumes that when given 'm', it converts to feet, and vice versa.
             If both input parameters were intended for identity (e.g., converting m back to m),
             this implementation returns the value directly as per standard conversion patterns 
             where only one direction is explicitly requested in typical utility functions unless specified otherwise.
    """
    
    # Conversion factors defined here based on 1 foot = 0.3048 meters exactly
    M_TO_FT_FACTOR = 3.280839895013123
    
    if unit == 'm':
        return length * M_TO_FT_FACTOR
    elif unit == 'ft':
        # Using reciprocal of factor: 1 / 0.3048 ≈ 3.28084...
        # Actually, to convert feet back to meters we divide by the ft-to-m conversion (or multiply by m/ft)
        return length * 0.3048
    
    raise ValueError(f"Unsupported unit: {unit}. Use 'm' or 'ft'.")

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration without interactive input
    samples = [
        ('1', 'm'),   # 1 meter to feet
        ('3.28084', 'm'), # Approximate conversion of 1 foot back (showing precision)
        ('5', 'ft'),  # 5 feet to meters
        ('1.524', 'ft') # Exact: 5 * 0.3048 = 1.524 meters -> convert to ft should be ~5 again
    ]

    for val_str, unit in samples:
        length_val = float(val_str)
        converted = convert_length(length_val, unit)
        print(f"Converted {length_val} {unit} to {converted:.10f}")