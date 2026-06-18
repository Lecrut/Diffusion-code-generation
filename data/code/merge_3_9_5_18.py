"""
Volume Converter Module

This module provides a standalone function to convert volumes from various units 
to liters with high precision using standard conversion factors.
Supported input units: 'liter', 'milliliter', 'kiloliter', 'gallon_us', 'quart_us', 
'pint_us', 'cup_us', 'fluid_ounce_us', 'barrel_oil', 'cubic_foot', 'cubic_meter'.

Conversion Factors to Liters (defined as constants for maximum precision):
- 1 liter = 1.0 L
- 1 milliliter = 1e-3 L
- 1 kiloliter = 1000.0 L
- 1 US gallon = ~3.785411784 L (exact: 231 * 64 / 1,000,000? No, standard is defined)
    Standard definition: 1 US fluid ounce = 29.5735295625 mL exactly.
    So 1 gal_us = 128 fl_oz * 29.5735295625e-3 L = 3.785411784 L exactly.
- 1 US quart = ~0.946352946 L (exact: gal_us / 4)
- 1 US pint = ~0.473176473 L (exact: gal_us / 8)
- 1 US cup = ~0.2498432365 L (exact: gal_us / 16)
- 1 US fluid ounce = ~0.0295735295625 L (exact definition above)
- 1 oil barrel = ~158.987294928 L (defined as exactly 42 US gallons) -> 42 * 3.785411784
- 1 cubic foot = ~28.316846592 L (exact: 0.3048^3 m^3 converted to liters, or derived from gallon definitions)
    Actually, exact definition via meters is safer for base SI consistency if needed, but US customary 
    are often defined relative to the inch which is defined as exactly 0.0254 m.
    So: 1 ft = 0.3048 m (exact). 1 cubic foot = (0.3048)^3 * 1000 L = 28.316846592 L exactly.
- 1 cubic meter = 1000.0 L

Note: The 'liter' unit is included for identity conversion, though it's technically a derived SI unit 
not part of the base seven units (kg, m, s, A, K, mol, cd). However, in volume context, it is standard.
"""

# Define precise conversion factors to Liters as constants

if __name__ == '__main__':
    pass
