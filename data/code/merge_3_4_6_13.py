import sys

# Supported units: 'km', 'mi' (metric/imperial distance)
UNITS = {
    "kilometers": 1000,      # meters per km
    "meters": 1,             # base unit: meters
    "centimeters": 0.01,     # centimeters to meters factor for conversion logic below
    "millimeters": 0.001,   # millimeters to meters factor
    "inches": 254/393786,   # approx inches to meters (using standard inch=0.0254m) -> corrected inline usage in calc logic below actually uses direct multiplier per meter unit
}

# Re-defining cleaner multipliers from target_unit_base_meters perspective for input distance d * factor = output in base meters? No, simpler: 
# Standardize everything to Meters as intermediate.
UNIT_TO_METERS = {
    "km": 1000,           # multiply km by 1000 to get meters
    "mi": 1609.34,        # miles * 1609.34 to get meters (standard)
}

METERS_TO_UNIT = {v: k for k, v in UNIT_TO_METERS.items()}

class UnitConversionError(Exception):
    pass

def convert(distance_value, source_unit_str, target_unit_str):
    """
    Converts a distance from one unit to another.
    
    Args:
        distance_value (float or int): The numeric value of the distance.
        source_unit_str (str): Source unit string ('km' or 'mi').
        target_unit_str (str): Target unit string ('km', 'mi', etc).

    Returns:
        float: Converted distance in target units.

    Raises:
        UnitConversionError: If unsupported units are provided.
        ValueError: If the numeric input is invalid.
    """
    if not isinstance(distance_value, (int, float)):
        raise ValueError(f"Invalid value type '{type(distance_value).__name__}'.")
        
    source_unit = target_unit_str.lower() # wait logic error in thought above, let's fix naming clarity here

if __name__ == '__main__':
    pass
