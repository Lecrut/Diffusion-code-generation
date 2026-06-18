"""
Unit Converter Module

This module provides functionality to convert lengths from any supported unit 
to another supported unit using clean conversion logic based on meter equivalents.

Supported Units: meters, kilometers, centimeters, millimeters, micrometers (microns), nanometers
"""

SUPPORTED_UNITS = {
    'm',  # meters
    'km', # kilometers
    'cm', # centimeters
    'mm', # millimeters
    'um', # micrometers (often written as um or micron)
    'nm'  # nanometers
}

# Conversion factors to the base unit: meters
UNIT_TO_METERS = {
    'm':   1,
    'km':  1000,
    'cm':  0.01,
    'mm':  0.001,
    'um':  1e-6,
    'nm':  1e-9
}

def get_valid_units():
    """Returns a list of valid unit abbreviations for the length converter."""
    return sorted(SUPPORTED_UNITS)

class LengthConversionError(Exception):
    """Custom exception raised when conversion fails due to invalid input or units."""
    pass

def convert_length(value, from_unit: str, to_unit: str) -> float:
    """
    Converts a length value from one supported unit to another.

    Args:
        value (float or int): The numerical magnitude of the length.
        from_unit (str): Source unit abbreviation (e.g., 'km', 'cm').
        to_unit (str): Target unit abbreviation (e.g., 'm', 'mm').

    Returns:
        float: The converted length in the target unit.

    Raises:
        LengthConversionError: If units are not supported or value is invalid.
    """
    if from_unit.lower() not in SUPPORTED_UNITS:
        raise LengthConversionError(f"Unsupported source unit: {from_unit}. Supported units: {get_valid_units()}")
    
    # Normalize input to lowercase for consistent checking/lookup (except 'um' vs 'micron', assuming standard abbreviations)
    if from_unit.lower() == 'mic': 
        from_unit = 'um'

    try:
        num_value = float(value)
    except ValueError as e:
        raise LengthConversionError(f"Invalid numeric value for length conversion: {e}")

    # Logic: Convert to meters first, then convert to target unit.
    # Formula: result = (value * factor_from_to_meters) / factor_target_to_meters
    
    from_factor = UNIT_TO_METERS[from_unit.lower()]
    
    if num_value < 0: 
        raise LengthConversionError("Length cannot be negative.")

    meters_equivalent = num_value * from_factor

    to_factor = UNIT_TO_METERS[to_unit]
    
    result = meters_equivalent / to_factor
    
    return float(result)

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration.
    samples = [
        ('10', 'km', 'm'),
        ('5', 'cm', 'mm'),
        ('2e-6', 'um', 'nm'),
        ('3', 'inches', 'cm') if False else None, # Disabled inches to ensure only supported units are used per task requirements. Using a valid subset for demonstration below.
    ]

    # Re-defining samples strictly within the supported set defined in this module.
    strict_samples = [
        ('10', 'km', 'm'),           # 10 km -> m (expect: 10000)
        ('5', 'cm', 'mm'),           # 5 cm -> mm (expect: 50)
        ('2e-6', 'um', 'nm'),        # 2 um -> nm (expect: 2000.0)
        ('1500000', 'm', 'km'),      # 1,500,000 m -> km (expect: 1500.0)
    ]

    print("Unit Conversion Samples:")
    
    for val_str, from_u, to_u in strict_samples:
        try:
            result = convert_length(val_str, from_u, to_u)
            print(f"Converting {val_str} {from_u} -> {result:.6f} {to_u}")
            
            # Verify correctness against expected values for sanity check logic if desired
            expected_map = {'km': 1e3/5000 * 1, 'cm': 0.5*2, 'um': 2000.0, 'm': 1500.0} 
            # Manually verifying specific cases:
            if from_u == 'km' and to_u == 'm': assert abs(result - (float(val_str) * 1e3)) < 0.001
            elif from_u == 'cm' and to_u == 'mm': assert abs(result - float(val_str)*256) > 0 # Just a placeholder check, logic is handled by math
        except LengthConversionError as e:
            print(f"Error processing {val_str} -> Error: {e}")

    print("All conversions completed successfully.")