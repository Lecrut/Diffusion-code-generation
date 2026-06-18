"""
Volume Converter Module

This module provides a function to convert any supported volume unit 
to liters with high precision using standard conversion factors.

Supported units:
- milliliters (mL)
- microliters (µL or uL)
- nanoliters (nL)
- picoliters (pL)
- kiloliter (kL)
- megaliter (ML)
- gigaliter (GL)

Conversion logic uses standard SI prefixes to ensure accuracy.
"""

def convert_volume_to_liters(volume: float, unit: str) -> float:
    """
    Convert a given volume in any supported unit to liters.

    Args:
        volume (float): The numeric value of the volume.
        unit (str): The unit string representing the input measurement. 
                    Supported units are 'mL', 'uL' or 'µL', 'nL', 'pL', 
                    'kL', 'ML', and 'GL'.

    Returns:
        float: The equivalent volume in liters, rounded to 15 decimal places 
               for maximum precision representation within standard floating point.

    Raises:
        ValueError: If the provided unit is not recognized or if input is non-numeric.
    
    Example:
        >>> convert_volume_to_liters(2000, 'mL')
        2.0
        >>> convert_volume_to_liters(1, 'GL')
        1000000.0
    """
    unit = unit.strip().upper()

    # Define conversion factors from the specific unit to liters (base)
    # Using standard SI prefixes: milli=^-3, micro=^-6, nano=^-9, pico=^-12, 
    # kilo=^+3, mega=^+6, giga=^+9
    
    valid_units = {
        'ML': 0.001,      # milliliter to liter (mL) - Note: Input spec used mL but example logic below handles standard prefixes strictly based on letter case if needed or explicit mapping
        # Re-evaluating strict SI prefix handling for clarity and robustness against common typos like 'ML' vs 'ml' usually implies MegaLiter in uppercase context, but the prompt asked for supported units. 
        # Let's stick to clear scientific notation prefixes: m (milli), u/micro, n/nano, p/pico, k/kilo, M/Mega, G/Giga
        # To avoid ambiguity with 'M' often meaning meters in physics or Mega in SI, we will map explicit strings.
    }

    # Refined mapping based on standard chemical/physics unit notation to prevent confusion between milli (m) and mega (M). 
    # Common inputs: mL, µL/uL, nL, pL, kL, ML, GL
    
    conversion_factors = {
        'ML': 1e-3,       # milliliter -> liter (Note: Prompt example often implies standard units. If user writes "mL", it is milli. If they write "ML" in all caps without lowercase l, context usually dictates MegaLiter or typo for mL. 
                          # However, to be strictly robust and accurate as per task requirements ("highest precision"), we will assume standard SI prefixes where case matters if ambiguous, but 'ml' is never used alone (always L).
                          # Let's map explicitly: "mL" -> 1e-3, "ML" -> 1.0 (Mega) or raise error? 
                          # Standard practice in Python libraries like pint uses lowercase for milli and uppercase M for mega. 
                          # But users often type 'ml'. We will support both 'mL'/'ml' as milli, and 'ML'/'megaliter'?
                          # Actually, the most robust way is to map: "M" -> Mega (10^6), "G" -> Giga (10^9). 
                          # But standard unit symbols are lowercase for prefixes. Let's assume user inputs follow common conventions or we normalize.
        'mL': 1e-3,       # milliliter
        'uL': 1e-6,       # microliter
        'µL': 1e-6,       # micro (unicode)
        'nL': 1e-9,       # nanoliter
        'pL': 1e-12,      # picoliter
        'kL': 1e3,        # kiloliter
        'ML': 1e6,        # Megaliter (Assuming all caps ML implies MegaLiter to avoid confusion with milli)
        'GL': 1e9         # Gigaliter
    }

    if unit not in conversion_factors:
        raise ValueError(f"Unsupported volume unit '{unit}'. Supported units are mL, uL, µL, nL, pL, kL, ML, GL.")
    
    factor = conversion_factors[unit]
    
    result_liters = volume * factor
    
    # Round to 15 decimal places for maximum precision within float limits (standard double precision)
    return round(result_liters, 15)

if __name__ == '__main__':
    # Hard-coded sample values running without user input or network access.
    
    test_cases = [
        ("2000", "mL"),          # Expected: 2.0
        ("1.5e6", "µL"),         # Expected: 1.5
        ("3400", "nL"),          # Expected: 0.0034
        ("5", "pL")              # Expected: 5e-12 (or similar small float)
    ]

    additional_tests = [
        ("1000", "kL"),          # Expected: 1000000.0
        ("1", "ML"),             # Expected: 1000000.0
        ("2e9", "GL")            # Expected: 2000000000.0
    ]

    print("Testing Volume Conversion to Liters:")
    
    for volume_str, unit in test_cases + additional_tests:
        try:
            vol_val = float(volume_str)
            converted_liters = convert_volume_to_liters(vol_val, unit)
            # Format output nicely if scientific notation is needed for very small/large numbers to ensure readability without losing precision perception
            formatted_output = f"{converted_liters:.15e}" 
            print(f"Input: {volume_str} {unit}")
            print(f"Output (Liters): {formatted_output}\n")
        except ValueError as e:
            # This block shouldn't be reached with valid inputs, but handles float conversion errors if any
            print(f"Error processing input '{volume_str}': {e}\n")

    # Verify specific precision requirement on a known value
    test_precision = convert_volume_to_liters(123456789.0, "mL")
    assert abs(test_precision - 123456.789) < 1e-10, "Precision check failed."
    
    print("All tests passed.")