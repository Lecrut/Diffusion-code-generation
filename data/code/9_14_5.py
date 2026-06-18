"""Volume Management Module.

This module provides functionality to convert between metric (liters, milliliters, cubic meters) 
and imperial (gallons) volume units using standard conversion factors.
It adheres to Python best practices including type hinting and is fully self-contained.
"""

# Conversion constants defined with high precision for accuracy
METRIC_TO_IMPERIAL_FACTOR = 0.26417205235814 # Liters per gallon (m³/L * gal/m³)
IMPERIAL_TO_METRIC_FACTOR = 3.785411784       # Gallons per liter

# Unit aliases for clarity in function signatures and return values
METRIC_UNITS = ('L', 'mL', 'm**3')
IMPERIAL_UNITS = ('gal',)

def _normalize_value(value: float, unit: str) -> tuple[float, str]:
    """Normalize a volume value to liters.

    Args:
        value (float): The numeric volume value.
        unit (str): The source unit string (e.g., 'L', 'mL', 'gal').

    Returns:
        tuple[float, str]: A tuple containing the normalized value in liters 
                           and the target unit ('L') as a string.
                           
    Raises:
        ValueError: If the provided unit is not recognized.
    """
    if isinstance(value, (int, float)):
        numeric_value = float(value)
    else:
        raise TypeError(f"Expected numeric value for volume, got {type(value).__name__}")

    source_unit_lower = unit.lower()

    # Convert to liters based on metric or imperial units
    try:
        if 'm' in source_unit_lower and not any(c.isdigit() for c in source_unit[:-1]): 
            # Handle cubic meters (e.g., "m**3" -> 0.001 L)
            target_value = numeric_value * 1000 ** 3 / 1_000_000 if '**' not in unit else numeric_value * 1000 ** 3
        elif source_unit_lower == 'l': 
            # Liters to liters (identity)
            target_value = numeric_value
        elif source_unit_lower == 'ml': 
            # Milliliters to liters
            target_value = numeric_value / 1000
        else:
            raise ValueError(f"Unsupported metric unit: {unit}")

    except Exception as e:
        if isinstance(e, (ValueError, TypeError)):
            raise
        raise RuntimeError("Unexpected error during normalization") from e
        
    # If it was an imperial gallon input, convert to liters first before finalizing
    try:
        if 'gal' in source_unit_lower and not any(c.isdigit() for c in unit[:-1]): 
             target_value = numeric_value * IMPERIAL_TO_METRIC_FACTOR
            
    except Exception as e:
         raise RuntimeError("Unexpected error during normalization") from e

    return float(target_value), "L"

def convert_metric_to_imperial(volume: int | float, source_unit: str) -> tuple[float, str]:
    """Convert a volume from metric units to imperial gallons.

    Args:
        volume (int | float): The numeric volume value in the specified unit.
        source_unit (str): The source metric unit string ('L', 'mL', or 'm³').

    Returns:
        tuple[float, str]: A tuple containing the converted volume in gallons 
                           and the target unit ('gal') as a string.

    Raises:
        ValueError: If the provided unit is not recognized.
        TypeError: If the input value is not numeric.
    """
    liters = _normalize_value(volume, source_unit)
    
    # Convert from liters to gallons using the pre-defined factor (Liters per gallon inverted logic handled in normalize for simplicity here or direct math)
    # Actually, IMPERIAL_TO_METRIC_FACTOR is gal/L? No, it's 3.78541... which means 1 L = 0.26417... gal and 1 gal = 3.78541 L.
    # Wait, let's re-verify: 
    # 1 US gallon ≈ 3.785 liters. So to go Liters -> Gallons we divide by 3.785 or multiply by (1/3.785).
    # My previous constant METRIC_TO_IMPERIAL_FACTOR was defined as "Liters per gallon" which is ~0.264. Correct.
    
    gallons = liters * METRIC_TO_IMPERIAL_FACTOR
    
    return float(gallons), 'gal'

def convert_imperial_to_metric(volume: int | float, source_unit: str) -> tuple[float, str]:
    """Convert a volume from imperial units to metric (liters).

    Args:
        volume (int | float): The numeric volume value in the specified unit.
        source_unit (str): The source imperial unit string ('gal').

    Returns:
        tuple[float, str]: A tuple containing the converted volume in liters 
                           and the target unit ('L') as a string.

    Raises:
        ValueError: If the provided unit is not recognized.
        TypeError: If the input value is not numeric.
    """
    # Since only 'gal' is supported for imperial, we can directly convert to Liters
    liters = volume * IMPERIAL_TO_METRIC_FACTOR
    
    return float(liters), "L"

def format_output(value: int | float) -> str:
    """Format a numeric value with appropriate precision.

    Args:
        value (int | float): The number to be formatted.

    Returns:
        str: A string representation of the number rounded to 6 decimal places 
             if it has decimals, otherwise as an integer string.
    """
    return f"{value:.6f}"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    
    samples = [
        {"input_value": 10, "source_unit": 'L', "target_type": "imperial"},
        {"input_value": 500, "source_unit": 'mL', "target_type": "imperial"},
        {"input_value": 2.5, "source_unit": 'gal', "target_type": "metric"},
        {"input_value": 1_000_000, "source_unit": 'm**3', "target_type": "imperial"},
    ]

    print("Volume Conversion Results")
    print("-" * 40)

    for sample in samples:
        val = sample["input_value"]
        src_unit = sample["source_unit"]
        
        if sample["target_type"] == "metric_to_imperial":
            result_val, target_unit = convert_metric_to_imperial(val, src_unit)
            print(f"Input: {val} {src_unit}")
            print(f"Output: {result_val:.6f} {target_unit}\n")

        elif sample["target_type"] == "imperial_to_metric":
            result_val, target_unit = convert_imperial_to_metric(val, src_unit)
            print(f"Input: {val} {src_unit}")
            print(f"Output: {result_val:.6f} {target_unit}\n")

    # Additional verification with edge cases if needed (optional based on strictness of "sample values", 
    # but good for completeness within the block)
    
    test_cases = [
        ("L", 1),
        ("mL", 0.5),
        ('gal', 2),
        ('m**3', 0.1),
    ]

    print("Verification Tests:")
    print("-" * 40)
    
    for unit, val in test_cases:
        # Test round trip logic roughly or just conversion display
        if 'L' in unit.lower() and not '**' in unit:
            g_val = convert_metric_to_imperial(val, unit)[0]
            l_back = convert_imperial_to_metric(g_val, 'gal')[0]
            
            print(f"{val} {unit} -> {g_val:.6f} gal")

        elif 'mL' in unit:
             g_val = convert_metric_to_imperial(val, unit)[0]
             l_back = convert_imperial_to_metric(g_val, 'gal')[0]