"""
Volume Converter Module

This module provides a function to convert any supported volume unit 
to liters with high precision using standard conversion factors.

Supported units:
- milliliters (ml)
- microliters (uL or µl)
- kiloliters (kL)
- cubic meters (m³)
- cubic centimeters (cm³)
- cubic decimeters (dm³) - equivalent to liters
- fluid ounces US (fl oz us)
- fluid ounces UK (fl oz uk)
- pints US (pt us)
- pints UK (pt uk)
- quarts US (qt us)
- quarts UK (qt uk)
- gallons US (gal us)
- gallons UK (gal uk)

Conversion factors are based on the International System of Units 
definitions and standard approximations for imperial units.
"""

def convert_volume_to_liters(volume: float, unit: str) -> float:
    """
    Convert a volume from any supported unit to liters.
    
    Parameters:
        volume (float): The volume value to convert. Must be non-negative.
        unit (str): The source unit of the volume. Supported units are 
                    'ml', 'uL', 'µl', 'kL', 'm3', 'cm3', 'dm3', 
                    'fl oz us', 'fl oz uk', 'pt us', 'pt uk', 
                    'qt us', 'qt uk', 'gal us', 'gal uk'.
    
    Returns:
        float: The volume converted to liters.
    
    Raises:
        ValueError: If the unit is not supported or if volume is negative.
    
    Examples:
        >>> convert_volume_to_liters(100, "ml")
        0.1
        >>> convert_volume_to_liters(264, "fl oz us")
        3.785411784
    """

if __name__ == '__main__':
    pass
