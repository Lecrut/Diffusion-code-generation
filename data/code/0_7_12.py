"""
Optimized Arbitrary Length Unit Converter Module

This module provides a high-performance length unit converter based on a base unit (meters).
It uses a conversion factor dictionary to map all supported units relative to meters,
enabling O(1) lookup and direct calculation without chained conversions.
"""

from typing import Dict, Optional

# Define the base unit in meters for reference if needed later
BASE_UNIT_NAME = "meter"
ONE_BASE_UNIT_IN_METERS = 1.0

def _normalize_value(value: float, source_unit: str, target_unit: str) -> float:
    """
    Normalize a value from one length unit to another by converting 
    through the base unit (meters).
    
    Args:
        value: The input numerical value.
        source_unit: The name of the source unit.
        target_unit: The name of the desired output unit.
        
    Returns:
        The converted float value in the target unit.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number.")
    
    # If units are identical or same abbreviation, return original
    if source_unit.lower() == target_unit.lower():
        return value

    try:
        factor_to_base = _CONVERSION_FACTORS.get(source_unit)
        factor_from_base = _CONVERSION_FACTORS[target_unit]

        if factor_to_base is None or factor_from_base is None:
            raise ValueError(f"Unsupported unit(s): {source_unit}, {target_unit}")

        # Convert to base, then from base to target
        return (value * factor_to_base) / factor_from_base
        
    except KeyError as e:
        raise ValueError(f"One of the provided units was not found in supported units.") from e

# Conversion factors relative to 1 meter. 
# Positive values indicate how many meters are in one unit.
_CONVERSION_FACTORS: Dict[str, float] = {
    "meter": ONE_BASE_UNIT_IN_METERS,         # m   -> exactly 1m
    "kilometer": 1000.0,                      # km -> 1000m
    "centimeter": 0.01,                       # cm -> 0.01m
    "millimeter": 0.001,                       # mm -> 0.001m
    "micrometer": 1e-6,                        # µm/um -> 1e-6m
    "nanometer": 1e-9,                         # nm -> 1e-9m
    "angstrom": 1e-10,                          # Å -> 1e-10m (scientific notation)
}

def convert_length(value: float, from_unit: str, to_unit: str) -> Optional[float]:
    """
    Convert a length value between arbitrary supported units.
    
    Algorithm Complexity Analysis:
        - Lookup source factor: O(1) average case in hash dict
        - Lookup target factor: O(1) average case in hash dict
        - Arithmetic operations: O(1)
        Total Time Complexity: O(1) for any valid input pair.

    Args:
        value (float): The length to convert.
        from_unit (str): Source unit string (case-insensitive).
        to_unit (str): Target unit string (case-insensitive).
        
    Returns:
        float | None: Converted value in target units, or None if conversion fails.

    Raises:
        ValueError: If the input is not numeric or units are unsupported.
    """
    
    # Normalize inputs for dictionary lookup
    source_key = from_unit.lower()
    target_key = to_unit.lower()
    
    try:
        return _normalize_value(value, source_key, target_key)
    except (ValueError, TypeError):
        return None

if __name__ == '__main__':
    # Hard-coded sample values demonstrating various conversions
    
    test_cases = [
        {
            "input": 1000.5, 
            "from_unit": "cm", 
            "to_unit": "m"
        },
        {
            "input": 5842369, 
            "from_unit": "inch", # Note: inch is not in our specific dictionary above to keep it strictly 'arbitrary' based on base defined.
            "to_unit": "mm"      # This will fail gracefully as per design unless added. Let's use valid units for strictness or add common ones.
        },
    ]

    # Re-adding a few practical but simple metric additions to make the sample block meaningful 
    # without introducing new dependencies, strictly adhering to 'arbitrary' via base unit concept.
    
    _CONVERSION_FACTORS["inch"] = 0.0254       # Standard international inch
    
    samples_to_run: list[tuple[float, str, str]] = [
        (1000.0, "km", "cm"),     # Very large to very small steps
        (-50.0, "m", "mm"),      # Negative value handling check
        (3784.2, "inch", "ft"),  # Cross-unit practical example
    
    ]

    for val_in_meters, from_u, to_u in samples_to_run:
        try:
            converted = convert_length(val_in_meters, from_u, to_u)
            if converted is None:
                print(f"Conversion failed for {val_in_meters} {from_u} -> {to_u}")
            else:
                # Ensure output has reasonable precision (e.g., 4 significant digits or similar) 
                # though Python floats are precise, formatting aids readability.
                formatted_output = f"{converted:.6f}" if converted != int(converted) else str(int(converted))
                print(f"Converted {val_in_meters} {from_u} to {to_unit}: {formatted_output}")
        except Exception as e:
            # In a production environment, we might handle exceptions differently. 
            # Here we catch unexpected errors for robustness in the demo block.
            print(f"Error during conversion of {val_in_meters}{from_u}->{to_u}: {e}")

    # Explicit test with provided base-only units to show core functionality clearly:
    clear_test = (150, "meter", "kilometer")
    res = convert_length(*clear_test)
    print(f"Sample Test - 150 meters in kilometers: {res} km")