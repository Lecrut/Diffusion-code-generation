"""
Optimized Arbitrary Length Unit Converter Module.

This module defines a base unit (meters) and uses a conversion factor dictionary
to handle conversions between any two length units supported by the system.
It ensures precision using Python's float type while maintaining code efficiency 
for arbitrary lengths within standard floating-point capabilities.
"""

class LengthConverter:
    """
    A class to convert arbitrary length units based on a base unit (meters).

    Attributes:
        base_unit (str): The reference unit, currently set to 'm' for meters.
        factors (dict): Dictionary mapping each supported unit to its factor relative 
                       to the base unit. E.g., {'km': 1000, 'cm': 0.01}.

    Methods:
        convert(value, from_unit, to_unit) -> float: Converts a value from one unit 
                                                    to another using conversion factors.
        
        get_supported_units() -> list[str]: Returns the list of supported units.
    """

# Define base unit as meters ('m') and its corresponding factor (1.0)
UNIT_BASE = 'm'

# Conversion factors relative to the base unit (meters)
CONVERSION_FACTORS = {
    'nm': 1e-9,   # nanometer
    'um': 1e-6,   # micrometer
    'mm': 0.001,  # millimeter
    'cm': 0.01,   # centimeter
    'm': 1.0,     # meter (base)
    'km': 1000,   # kilometer
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Converts a length value from one unit to another.

    Args:
        value (float): The numerical value of the length in 'from_unit'.
        from_unit (str): Source unit string (must be supported).
        to_unit (str): Target unit string (must be supported).

    Returns:
        float: Converted value in 'to_unit'.

    Raises:
        ValueError: If input units are not recognized or if the provided 
                   numeric value is invalid.
    """
    # Validate inputs and retrieve factors for both source and target units
    unit1 = from_unit.lower()
    unit2 = to_unit.lower()

    if unit1 not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported conversion factor '{unit1}'. Supported units are " + 
                        ', '.join(CONVERSION_FACTORS.keys()))
    
    if unit2 not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported conversion factor '{unit2}'. Supported units are " + 
                        ', '.join(CONVERSION_FACTORS.keys()))

    # Convert to base unit (meters) then convert from meters to target unit
    value_in_base = value * CONVERSION_FACTORS[unit1]
    result = value_in_base / CONVERSION_FACTORS[unit2]

    return result

def get_supported_units() -> list:
    """
    Returns the list of supported length units.

    Returns:
        List[str]: Sorted alphabetically for consistency, e.g., ['km', 'm', ...].
    """
    return sorted(CONVERSION_FACTORS.keys())

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input
    
    test_cases = [
        {'value': 10.5, 'from_unit': 'km', 'to_unit': 'm'},      # Kilometers to meters
        {'value': 254367.89, 'from_unit': 'mm', 'to_unit': 'cm'},# Millimeters to centimeters
        {'value': 100, 'from_unit': 'um', 'to_unit': 'nm'},      # Micrometers to nanometers
        {'value': 500.234, 'from_unit': 'm', 'to_unit': 'km'},   # Meters to kilometers
    ]

    print("Supported Units:", get_supported_units())
    
    for case in test_cases:
        value = case['value']
        source = case['from_unit']
        target = case['to_unit']
        
        try:
            converted_result = convert_length(value, source, target)
            
            # Print formatted output showing the conversion process clearly
            print(f"Conversion from {source} to {target}:")
            print(f"{value:.4f} {source} =", f"{converted_result:.6f} {target}")
        except ValueError as e:
            print(f"Error during conversion for inputs ({value}, '{source}', '{target}'):", str(e))

    # Additional edge case test with unsupported unit to verify error handling
    try:
        convert_length(10, 'ft', 'in')  # Feet is not supported in this dictionary
    except ValueError as e:
        print("\nError (Expected):", str(e))