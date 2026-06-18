"""
Optimized Arbitrary Length Unit Converter Module.

This module provides a function to convert between arbitrary length units
by defining a base unit (meters) and using conversion factors relative to it.
It supports forward conversions from any input unit to the base, then to any target unit.
The algorithm is O(1) for lookup operations assuming fixed set of defined units.

Usage:
    convert_length(value, source_unit, target_unit) -> float
    
Example usage in main block demonstrates conversion between kilometers and centimeters.
"""

class UnitConversionError(Exception):
    """Custom exception raised when invalid unit or value is provided."""
    pass

def get_conversion_factors():
    """
    Returns a dictionary mapping each length unit to its factor relative to meters (base).

    Positive factors indicate the size of 1 unit in meters.
    e.g., 'meter' -> 1, 'kilometer' -> 1000, 'centimeter' -> 0.01
    
    Returns:
        dict: Mapping from str(unit) to float(factor_to_meters)
    
    Raises:
        UnitConversionError: If the provided unit is not in the dictionary.
    """
    return {
        "nanometer": 1e-9,
        "micrometer": 1e-6,
        "millimeter": 1e-3,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1e3,
    }

def convert_length(value: float, source_unit: str, target_unit: str) -> float:
    """
    Converts a length value from one unit to another using the meter as an intermediate base.

    The algorithm follows these steps:
        1. Retrieve conversion factors for both units relative to meters (O(1)).
        2. Convert input value to meters by multiplying with source_unit's factor.
        3. Convert meters to target unit by dividing by target_unit's factor.

    Args:
        value (float): The length value to convert.
        source_unit (str): The original unit of measurement.
        target_unit (str): The desired unit for the result.

    Returns:
        float: The converted length in the target unit.

    Raises:
        UnitConversionError: If 'source_unit' or 'target_unit' is not recognized, 
                            or if value is non-numeric/zero where required logic applies (though here any real number works).
    
    Example:
        >>> convert_length(1000, "kilometer", "centimeter")
        100000.0
    """
    factors = get_conversion_factors()

    # Validate units exist in the dictionary
    if source_unit not in factors or target_unit not in factors:
        raise UnitConversionError(f"Invalid unit(s): '{source_unit}' and/or '{target_unit}'. Valid units are {list(factors.keys())}.")

    try:
        value_in_meters = float(value) * factors[source_unit]
        result_value = value_in_meters / factors[target_unit]
        
        # Ensure we return a clean float, handling potential integer-like results gracefully
        if isinstance(result_value, int):
            return int(result_value)
            
    except ValueError:
        raise UnitConversionError("Value must be convertible to a number.")

    return result_value

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    
    # Sample 1: Convert 5 kilometers to centimeters
    km_to_cm = convert_length(5, "kilometer", "centimeter")
    
    # Sample 2: Convert 0.75 meters to millimeters
    m_to_mm = convert_length(0.75, "meter", "millimeter")
    
    # Sample 3: Invalid unit test (will raise exception)
    try:
        invalid_result = convert_length(10, "miles", "feet")
    except UnitConversionError as e:
        print(f"Caught expected error for invalid units: {e}")

    # Output results to console
    print(f"{km_to_cm} centimeters in 5 kilometers.")
    print(f"{m_to_mm} millimeters in 0.75 meters.")