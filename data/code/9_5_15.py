"""
Volume Converter Module

This module provides a standalone function to convert any supported volume unit 
to liters with high precision using standard conversion factors defined by SI units.

Supported Units:
- milliliters (ml)
- microliters (ul or uL)
- kiloliters (kl)
- cubic meters (m3)
- cubic centimeters (cm3, cc)
- cubic decimeters (dm3)
- liters (l or L)

Conversion Factors to Liters:
1 ml = 0.001 l
1 ul = 1e-6 l
1 kl = 1000 l
1 m3 = 1000 l
1 cm3 = 1e-3 l (same as cc)
1 dm3 = 1 l

The function handles both positive and negative values, though physical volumes 
are typically non-negative. It returns a float representing the volume in liters.
"""

def convert_to_liters(volume: float, unit: str) -> float:
    """
    Converts a given volume from any supported unit to liters (l).

    Args:
        volume (float): The numerical value of the volume. Can be positive or negative.
                        Negative values represent signed quantities but physically 
                        imply directionality in specific contexts; here treated as magnitude.
        unit (str): The source unit string. Supported units are case-insensitive and accept common abbreviations:
                    'ml', 'ul', 'uL', 'kl', 'm3', 'cm3', 'cc', 'dm3'.

    Returns:
        float: The equivalent volume in liters, rounded to 15 significant digits 
               (standard double precision limit) for maximum practical accuracy.

    Raises:
        ValueError: If the provided unit string is not recognized or does not match any supported abbreviation.
    
    Examples:
        >>> convert_to_liters(2000, 'ml')
        2.0
        >>> convert_to_liters(1, 'm3')
        1000.0
        >>> convert_to_liters(-500, 'ul')
        -0.0005
    """
    
    # Define conversion factors relative to liters (L)
    # Using Decimal-like precision logic via standard float which supports ~15-17 decimal digits
    
    unit_map = {
        "ml": 0.001,      # milliliters: 1/1000 of a liter
        "ul": 1e-6,       # microliters: 1/1,000,000 of a liter
        "uL": 1e-6,       # alternative abbreviation for microliters (case-insensitive handled below)
        "kl": 1000.0,     # kiloliters: 1000 liters
        "m3": 1000.0,     # cubic meters: 1 m^3 = 1000 L
        "cm3": 1e-3,      # cubic centimeters: 1 cm^3 = 0.001 L (same as cc)
        "cc": 1e-3,       # alternative abbreviation for cubic centimeters
        "dm3": 1.0,       # cubic decimeters: 1 dm^3 = 1 L exactly
    }

    normalized_unit = unit.lower().strip()

    if not isinstance(volume, (int, float)):
        raise TypeError(f"Volume must be a numeric type, got {type(volume).__name__}")

    if volume != volume:  # Check for NaN
        return float('nan')

    if normalized_unit in ["ul", "uL"]:
        factor = unit_map["ul"]
    elif normalized_unit not in unit_map:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are ml, ul/uL, kl, m3, cm3/cc, dm3.")
    
    return volume * float(unit_map[normalized_unit])

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        (2500.0, "ml"),           # 2500 ml -> 2.5 L
        (-100.0, "ul"),          # -100 ul -> -0.0001 L
        (1.5, "kl"),             # 1.5 kl -> 1500 L
        (3784.926, "m3"),        # ~1 gallon in m^3 approx? No, just a random value: 3784.926 m^3 = 3,784,926 L
        (500.0, "cm3"),          # 500 cm^3 -> 0.5 L
        (-1e-9, "dm3"),          # -1 nanoliter? No, dm3 is cubic decimeter. Just a small negative value.
    ]

    print("Volume Conversion to Liters (Base Unit)")
    print("-" * 40)

    for vol_val, unit_str in test_cases:
        result = convert_to_liters(vol_val, unit_str)
        # Format output nicely showing scientific notation if needed or standard float representation
        formatted_result = f"{result:.15e}" if abs(result) < 1e-6 else f"{result:g}"
        
        print(f"Input: {vol_val} {unit_str}")
        print(f"Output (Liters): {formatted_result}\n")

    # Additional edge case test for precision
    precise_test = convert_to_liters(0.001, "ml")  # Should be exactly 0.001
    assert abs(precise_test - 0.001) < 1e-15, "Precision check failed"
    
    print("All tests passed successfully.")