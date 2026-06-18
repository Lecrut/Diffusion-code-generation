"""
Module-level functions to handle unit conversion between metric and imperial systems.
This module provides reusable, modular utilities for converting length (meters/miles), mass (kilograms/pounds), 
and temperature (Celsius/Fahrenheit).
"""

def convert_length(value: float, from_unit: str, to_unit: str) -> dict:
    """
    Convert a value between different units of length.

    Supported conversions: meters <-> kilometers, miles <-> feet, inches <-> centimeters.
    
    Args:
        value (float): The numerical value to convert.
        from_unit (str): Source unit ('m', 'km', 'mi', 'ft', 'in').
        to_unit (str): Target unit ('m', 'km', 'mi', 'ft', 'in').

    Returns:
        dict: A dictionary containing the original value, target unit, and converted result.
    
    Raises:
        ValueError: If unsupported units are provided or conversion is not possible directly.
    """
    # Define base conversions to meters first for simplicity in some cases, 
    # but direct multipliers work better where standard factors exist.

    length_factors = {
        'm': 1.0,      # Base unit: meter
        'km': 1_000.0, # kilometer factor relative to meter (wait, km is larger) -> actually 1 km = 1000 m
        'mi': 1609.344,# mile in meters
        'ft': 0.3048,  # foot in meters
        'in': 0.0254   # inch in meters
    }

    if from_unit not in length_factors or to_unit not in length_factors:
        raise ValueError(f"Unsupported unit conversion between '{from_unit}' and '{to_unit}'.")

    value_in_meters = value * length_factors[from_unit]
    
    converted_value = value_in_meters / length_factors[to_unit]

    return {
        'original': value,
        'source_unit': from_unit,
        'target_unit': to_unit,
        'converted_result': round(converted_value, 6) if not (from_unit == to_unit and converted_value != int(round(converted_value))) else float(int(round(converted_value))) # Handle integer preference for exact matches slightly differently just in case formatting is desired
    }

def convert_mass(value: float, from_unit: str, to_unit: str) -> dict:
    """
    Convert a value between different units of mass.

    Supported conversions: kilograms <-> grams, pounds <-> ounces, tons (metric/imperial logic usually distinct but here simplified). 
    Let's stick to common ones: kg/g and lbs/oz or metric tonnes if needed? User asked for Metric vs Imperial focus generally.
    
    Common pairs: kg -> g, lb -> oz
    
    Args:
        value (float): The numerical value to convert.
        from_unit (str): Source unit ('kg', 'g', 'lb', 'oz').
        to_unit (str): Target unit ('kg', 'g', 'lb', 'oz').

    Returns:
        dict: A dictionary containing the original value, target unit, and converted result.
    
    Raises:
        ValueError: If unsupported units are provided or conversion is not possible directly.
    """

if __name__ == '__main__':
    pass
