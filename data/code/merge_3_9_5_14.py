"""
Volume Converter Module: Converts any supported volume unit to liters (L) with high precision.

Supported Units:
- milliliters (mL, ml, centiliter, cL, dCl) -> 1 mL = 0.001 L; 1 cL = 0.01 L
- microliters (µL, uL) -> 1 µL = 1e-6 L
- liters (L, l, litre) -> Base unit (factor: 1)
- hectoliters (hL), dekaliters (dL), kiloliters (kL or kl)
    - hL = 100 L; dL = 10 L; kL = 1000 L
- gallons (gal, US liquid): -> 1 gal ≈ 3.785411784 L
- quarts (qt, US liquid)     : -> 1 qt ≈ 0.946352946 L
- pints (pt, US liquid)      : -> 1 pt ≈ 0.473176473 L
- fluid ounces (fl oz, US)   : -> 1 fl oz ≈ 0.0295735295625 L

Precision: Conversion factors are chosen to be accurate for double-precision floating point arithmetic.
"""

def convert_volume_to_liters(volume_value: float | int, unit_str: str) -> float:
    """
    Converts a given volume in any supported unit to liters (L).
    
    Args:
        volume_value (float|int): The numerical value of the volume.
        unit_str (str): A string representing the unit (e.g., 'mL', 'gal'). 
                        Supported units are case-insensitive and accept common abbreviations/symbols.

    Returns:
        float: The equivalent volume in liters, accurate to standard double precision limits for these constants.
    
    Raises:
        ValueError: If the input value is not a number or if an unsupported unit string is provided (after normalization).
    """
    # Normalize inputs and define conversion factors relative to Liters
    
    try:
        numeric_value = float(volume_value)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid volume value '{volume_value}'. Expected a number.")

    
    unit_lower = unit_str.lower().strip() if isinstance(unit_str, str) else ""
    
    # Dictionary of conversion factors to Liters
    # Key is the normalized string key; Value is liters per 1 unit.

if __name__ == '__main__':
    pass
