import argparse

CONVERSION_FACTORS = {
    ('liters', 'milliliters'): 1000.0,
    ('milliliters', 'liters'): 1.0 / 1000.0,
    ('liters', 'gallons'): 0.264172,
    ('gallons', 'liters'): 1.0 / 0.264172,
    ('gallons', 'liters'): 3.78541,
    ('liters', 'gallons'): 1.0 / 3.78541,
    ('cups', 'milliliters'): 236.588,
    ('milliliters', 'cups'): 1.0 / 236.588,
    ('cups', 'liters'): 0.236588,
    ('liters', 'cups'): 1.0 / 0.236588,
    ('tablespoons', 'milliliters'): 14.7868,
    ('milliliters', 'tablespoons'): 1.0 / 14.7868,
    ('teaspoons', 'milliliters'): 4.92892,
    ('milliliters', 'teaspoons'): 1.0 / 4.92892,
    ('fluid_ounces', 'milliliters'): 29.5735,
    ('milliliters', 'fluid_ounces'): 1.0 / 29.5735,
}

SUPPORTED_UNITS = ['liters', 'milliliters', 'gallons', 'cups', 'tablespoons', 'teaspoons', 'fluid_ounces']

def convert_volume(value, from_unit, to_unit):
    if from_unit not in SUPPORTED_UNITS or to_unit not in SUPPORTED_UNITS:
        raise ValueError(f"Unsupported unit. Supported: {SUPPORTED_UNITS}")
    
    if from_unit == to_unit:
        return value
    
    key = (from_unit, to_unit)
    if key not in CONVERSION_FACTORS:
        raise ValueError(f"No direct conversion factor found for {from_unit} to {to_unit}")
    
    factor = CONVERSION_FACTORS[key]
    return value * factor

def parse_args():
    parser = argparse.ArgumentParser(description='Convert volume units.')
    parser.add_argument('volume', type=float, help='Input volume value')
    parser.add_argument('from_unit', type=str, help='Input unit')
    parser.add_argument('to_unit', type=str, help='Output unit')
    return parser.parse_args()

if __name__ == '__main__':
    try:
        result = convert_volume(1.0, 'gallons', 'liters')
        print(result)
    except ValueError as e:
        print(e)