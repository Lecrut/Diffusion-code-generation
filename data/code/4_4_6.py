"""
Unit Conversion Module: Metric to Imperial Converter.

This module provides a set of functions to handle unit conversions between 
the metric system (SI) and the imperial/US customary systems, focusing on modularity 
and reusability. It supports length, mass, volume, temperature, area, and speed conversions.

All conversion factors are defined as constants within this module for consistency.
"""

# Conversion Constants
METRIC_TO_IMPERIAL_FACTORS = {
    'length': {'m_to_ft': 3.28084, 'cm_to_inch': 0.3937},
    'mass': {'kg_to_lb': 2.20462, 'g_to_oz': 0.035274},
    'volume': {'l_to_gal_us': 0.264172, 'ml_to_fl_oz_us': 0.033814},
    'area': {'m2_to_ft2': 10.7639, 'ha_to_acre': 2.47105},
    'speed': {'kmh_to_mph': 0.621371},
}

TEMPERATURE_CONVERSIONS = {
    'celsius_to_fahrenheit': lambda c: (c * 9/5) + 32,
    'fahrenheit_to_celsius': lambda f: (f - 32) * 5/9,
}

def convert_length(metric_value, metric_unit, imperial_unit):
    """
    Convert a length value from one metric unit to an imperial unit.

    Supported Metric Units: m, cm
    Supported Imperial Units: ft, inch
    
    Args:
        metric_value (float or int): The value in the source metric unit.
        metric_unit (str): Source unit ('m' for meters, 'cm' for centimeters).
        imperial_unit (str): Target unit ('ft' for feet, 'inch' for inches).

    Returns:
        float: Converted value in the target imperial unit.

    Raises:
        ValueError: If unsupported units are provided.
    """
    if metric_unit not in ['m', 'cm'] or imperial_unit not in ['ft', 'inch']:
        raise ValueError(f"Unsupported units. Metric must be m/cm, Imperial must be ft/inch.")
    
    # Convert to meters first as a base reference for length
    value_in_meters = metric_value if metric_unit == 'm' else metric_value / 100
    
    factor = METRIC_TO_IMPERIAL_FACTORS['length']
    
    if imperial_unit == 'ft':
        return value_in_meters * factor['m_to_ft']
    elif imperial_unit == 'inch':
        # Convert meters to inches directly using standard conversion (1 m = 39.3701 in)
        # Or via cm: 1 m = 100 cm, 1 inch = 2.54 cm -> factor is approx 39.3701
        return value_in_meters * METRIC_TO_IMPERIAL_FACTORS['length']['cm_to_inch'] * 100

def convert_mass(metric_value, metric_unit, imperial_unit):
    """
    Convert a mass value from one metric unit to an imperial unit.

    Supported Metric Units: kg, g
    Supported Imperial Units: lb, oz
    
    Args:
        metric_value (float or int): The value in the source metric unit.
        metric_unit (str): Source unit ('kg' for kilograms, 'g' for grams).
        imperial_unit (str): Target unit ('lb' for pounds, 'oz' for ounces).

    Returns:
        float: Converted value in the target imperial unit.

    Raises:
        ValueError: If unsupported units are provided.
    """
    if metric_unit not in ['kg', 'g'] or imperial_unit not in ['lb', 'oz']:
        raise ValueError(f"Unsupported units. Metric must be kg/g, Imperial must be lb/oz.")
    
    # Convert to kilograms first as a base reference for mass
    value_in_kg = metric_value if metric_unit == 'kg' else metric_value / 1000
    
    factor = METRIC_TO_IMPERIAL_FACTORS['mass']
    
    if imperial_unit == 'lb':
        return value_in_kg * factor['kg_to_lb']
    elif imperial_unit == 'oz':
        # Convert kg to oz directly: 1 kg ≈ 35.274 oz
        return value_in_kg * METRIC_TO_IMPERIAL_FACTORS['mass']['g_to_oz'] * 1000

def convert_volume(metric_value, metric_unit, imperial_unit):
    """
    Convert a volume value from one metric unit to an imperial (US) unit.

    Supported Metric Units: l, ml
    Supported Imperial Units: gal_us, fl_oz_us
    
    Args:
        metric_value (float or int): The value in the source metric unit.
        metric_unit (str): Source unit ('l' for liters, 'ml' for milliliters).
        imperial_unit (str): Target unit ('gal_us' for US gallons, 'fl_oz_us' for fluid ounces).

    Returns:
        float: Converted value in the target imperial unit.

    Raises:
        ValueError: If unsupported units are provided.
    """
    if metric_unit not in ['l', 'ml'] or imperial_unit not in ['gal_us', 'fl_oz_us']:
        raise ValueError(f"Unsupported units. Metric must be l/ml, Imperial must be gal_us/fl_oz_us.")
    
    # Convert to liters first as a base reference for volume
    value_in_liters = metric_value if metric_unit == 'l' else metric_value / 1000
    
    factor = METRIC_TO_IMPERIAL_FACTORS['volume']
    
    if imperial_unit == 'gal_us':
        return value_in_liters * factor['l_to_gal_us']
    elif imperial_unit == 'fl_oz_us':
        # Convert liters to fl oz: 1 l ≈ 33.814 fl oz
        return value_in_liters * METRIC_TO_IMPERIAL_FACTORS['volume']['ml_to_fl_oz_us'] * 1000

def convert_area(metric_value, metric_unit, imperial_unit):
    """
    Convert an area value from one metric unit to an imperial (US) unit.

    Supported Metric Units: m2, ha
    Supported Imperial Units: ft2, acre
    
    Args:
        metric_value (float or int): The value in the source metric unit.
        metric_unit (str): Source unit ('m2' for square meters, 'ha' for hectares).
        imperial_unit (str): Target unit ('ft2' for square feet, 'acre').

    Returns:
        float: Converted value in the target imperial unit.

    Raises:
        ValueError: If unsupported units are provided.
    """
    if metric_unit not in ['m2', 'ha'] or imperial_unit not in ['ft2', 'acre']:
        raise ValueError(f"Unsupported units. Metric must be m2/ha, Imperial must be ft2/acre.")
    
    # Convert to square meters first as a base reference for area
    value_in_m2 = metric_value if metric_unit == 'm2' else metric_value * 10000
    
    factor = METRIC_TO_IMPERIAL_FACTORS['area']
    
    if imperial_unit == 'ft2':
        return value_in_m2 * factor['m2_to_ft2']
    elif imperial_unit == 'acre':
        # Convert m2 to acres: 1 ha ≈ 2.47105 acre, so 1 m2 = 0.000247105 acre
        return value_in_m2 * METRIC_TO_IMPERIAL_FACTORS['area']['ha_to_acre'] / 10000

def convert_speed(metric_value, metric_unit, imperial_unit):
    """
    Convert a speed value from one metric unit to an imperial (US) unit.

    Supported Metric Units: kmh
    Supported Imperial Units: mph
    
    Args:
        metric_value (float or int): The value in the source metric unit.
        metric_unit (str): Source unit ('kmh' for kilometers per hour).
        imperial_unit (str): Target unit ('mph').

    Returns:
        float: Converted speed in miles per hour.

    Raises:
        ValueError: If unsupported units are provided.
    """
    if metric_unit != 'kmh' or imperial_unit != 'mph':
        raise

if __name__ == '__main__':
    pass
