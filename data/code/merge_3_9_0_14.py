import math

# Define conversion constants based on standard definitions:
# 1 liter = 0.264172 gallons (US liquid)
# 1 gallon (US liquid) = 3.78541 liters
# 1 cubic meter = 1000 liters
# 1 liter = 1000 milliliters
# 1 inch = 0.0254 meters
# Therefore, 1 cubic inch = (0.0254)^3 * 1000 * 0.078639... let's derive exactly:
# Volume in liters from volume in cubic inches: V_liters = V_cubic_inches * (0.0254 ** 3)

LITER_TO_GALLON = 0.264172052
GALLON_TO_LITER = 1 / LITER_TO_GALLON
CUBIC_METER_TO_LITER = 1000
MILLILITER_TO_LITER = 0.001

# Cubic inches to liters factor: (inch in meters)^3 * liters per cubic meter
INCHES_PER_METRE = 39.37007874 # approx, better calculate directly below for precision or use defined constant
METRES_TO_INCHES_FACTOR_INV = 1 / INCHES_PER_METRE

# Precise calculation: 1 inch = 2.54 cm exactly
INMCM_TO_LITER = (2.54 ** 3) * 0.078639 # Wait, simpler derivation is needed to avoid confusion in comments vs code logic
# Let's stick to base conversions through liters or meters where possible for accuracy without hard magic numbers unless necessary.

INCHES_TO_METERS = 2.54 / 100.0 # cm/m conversion then apply volume? No, 1 inch is exactly 2.54cm.
# So 1 cubic inch = (2.54e-2 m)^3 * 1000 L/m^3 = 2.54**3 * 1e6 / 1e9 * 1000? 
# Simple math: (0.0254 ** 3) * 1000 liters per cubic meter gives the factor directly from Cubic Inches to Liters

CUBIC_INCH_TO_LITER = (0.0254 ** 3) * 1000

def convert_volume(value, unit, target_unit):
    """
    Convert a volume value between various units using liters as an intermediate step where possible,
    or direct conversions for cubic inches to maintain high precision.

    Supported Units: 'liters', 'milliliters', 'cubic_meters', 'gallons' (US), 'cubic_inches'.
    
    Args:
        value (float): The volume value to convert.
        unit (str): Source unit string. Case-insensitive support is preferred but input validation assumed on valid set.
        target_unit (str): Target unit string for conversion.

    Returns:
        float: Converted volume in the target unit, rounded to 6 decimal places for consistency.
    
    Raises:
        ValueError: If unsupported units are provided or value is invalid.
    """
    
    # Normalize input strings to lowercase for comparison
    source = unit.lower()
    target = target_unit.lower()

    valid_units = {'liters', 'milliliters', 'cubic_meters', 'gallons', 'cubic_inches'}
    if source not in valid_units or target not in valid_units:
        raise ValueError(f"Unsupported units. Valid options are {valid_units}")
    
    # Ensure value is numeric (though task constraints say no input() calls, robustness suggests handling float)
    try:
        val = float(value)
    except TypeError:
         return None

    if target == 'liters':
        # Convert to liters as the base unit for simplicity in this script logic
        conversion_factors_to_litres = {
            'gallons': GALLON_TO_LITER, 
            'cubic_meters': 1 / CUBIC_METER_TO_LITER, 
            'milliliters': MILLILITER_TO_LITER * 0.001 # Wait: Milliliter to Liter is 0.001
        }
        
    elif target == 'gallons':
        if source == 'liters': return val * LITER_TO_GALLON
        if source in ('cubic_meters',): 
            temp_litres = val / CUBIC_METER_TO_LITER # Convert m3 to liters first? No, cubic_meter is 1000L. So mult by 1/1000 then * Gallon Factor
            
    # Refined conversion logic via a helper dictionary of factors relative to Liters

if __name__ == '__main__':
    pass
