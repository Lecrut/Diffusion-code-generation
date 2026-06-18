import math

# Supported units: meters, centimeters, millimeters, kilometers, micrometers
UNITS = {
    "m": 1e0,      # base unit (meter)
    "cm": 1e-2,    # centimeter
    "mm": 1e-3,    # millimeter
    "km": 1e3,     # kilometer
    "um": 1e-6,    # micrometer
}

def parse_unit(unit_str):
    """Parse a unit string to its base multiplier. Returns None if invalid."""
    return UNITS.get(unit_str.lower())

def convert_length(value, source_unit, target_unit):
    """
    Convert length from one supported unit to another.
    
    Args:
        value (float or int): The numerical value of the length.
        source_unit (str): Source unit string (e.g., 'm', 'cm').
        target_unit (str): Target unit string (e.g., 'km', 'mm').
        
    Returns:
        float: Converted length in the target unit.
    
    Raises:
        ValueError: If units are not supported or value is invalid.
    """
    if source_unit.lower() == "":
        raise ValueError("Source unit cannot be empty.")

    # Validate input types and values
    try:
        val = float(value)
    except (TypeError, ValueError):
        raise TypeError(f"Value must be a number, got {type(value).__name__}") from None
    
    if not math.isfinite(val):
        raise ValueError("Length value must be finite.")

    source_multiplier = parse_unit(source_unit.lower())
    target_multiplier = parse_unit(target_unit.lower())

    # Check for invalid units
    if source_multiplier is None or target_multiplier is None:
        valid_units = list(UNITS.keys())
        raise ValueError(f"Unsupported unit(s). Supported units are {valid_units}.")

    # Convert to base (meters) then to target
    length_in_base_meters = val * source_multiplier
    converted_value = length_in_base_meters / target_multiplier
    
    return converted_value

if __name__ == '__main__':
    # Hard-coded sample values for testing conversion logic
    test_cases = [
        {"value": 1, "source_unit": "m", "target_unit": "km"},           # Expected: 0.001
        {"value": 500, "source_unit": "cm", "target_unit": "mm"},       # Expected: 5000
        {"value": 2, "source_unit": "um", "target_unit": "m"},          # Expected: 0.000002
        {"value": 1000, "source_unit": "km", "target_unit": "cm"},      # Expected: 1e8
    ]

    for case in test_cases:
        result = convert_length(case["value"], case["source_unit"], case["target_unit"])
        print(f"Converted {case['value']} {case['source_unit']!r} to {result:.20f} {case['target_unit']!r}")

    # Additional error handling test (commented out as per requirement: no interactive input)
    # Uncommenting below would trigger an exception, which is expected behavior for invalid inputs.
    # try:
    #     convert_length(10, "invalid", "m")
    # except ValueError as e:
    #     print(f"Caught expected error: {e}")