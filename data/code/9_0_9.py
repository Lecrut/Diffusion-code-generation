import math

CONVERSION_FACTORS = {
    'liter': 1.0,
    'milliliter': 0.001,
    'cubic_meter': 1000.0,
    'gallon': 3.78541,
    'cubic_inch': 0.0163871,
}

UNIT_LABELS = {
    'liter': 'Liters',
    'milliliter': 'Milliliters',
    'cubic_meter': 'Cubic Meters',
    'gallon': 'Gallons',
    'cubic_inch': 'Cubic Inches',
}

def convert_volume(value, from_unit, to_unit):
    if from_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unknown target unit: {to_unit}")
    
    value_in_liters = value * CONVERSION_FACTORS[from_unit]
    converted_value = value_in_liters / CONVERSION_FACTORS[to_unit]
    return converted_value

def print_conversions(value, from_unit):
    results = {}
    for unit in CONVERSION_FACTORS:
        if unit == from_unit:
            results[unit] = value
        else:
            results[unit] = convert_volume(value, from_unit, unit)
    return results

if __name__ == '__main__':
    sample_value = 1.5
    sample_unit = 'gallon'
    
    converted_values = print_conversions(sample_value, sample_unit)
    
    for unit, val in converted_values.items():
        print(f"{UNIT_LABELS[unit]}: {val:.6f}")