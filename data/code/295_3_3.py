import math
def convert_to_base(value, unit):
    conversion_factors = {
        'length': {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'inch': 0.0254,
            'foot': 0.3048,
            'mile': 1609.34
        },
        'mass': {
            'kilogram': 1.0,
            'gram': 0.001,
            'milligram': 0.000001,
            'pound': 0.453592,
            'ounce': 0.0283495
        },
        'volume': {
            'liter': 1.0,
            'milliliter': 0.001,
            'cubic_meter': 1.0,
            'cubic_centimeter': 0.000001
        }
    }
    if unit not in conversion_factors:
        return value, "Error: Unsupported unit"
    if value == 0:
        return 0.0, unit
    if unit == 'length':
        to_meter = conversion_factors['length']['meter']
        if unit == 'meter':
            return float(value), 'meter'
        elif unit == 'kilometer':
            return value * to_meter, 'meter'
        elif unit == 'centimeter':
            return value * to_meter, 'meter'
        elif unit == 'millimeter':
            return value * to_meter, 'meter'
        elif unit == 'inch':
            return value * to_meter, 'meter'
        elif unit == 'foot':
            return value * to_meter, 'meter'
        elif unit == 'mile':
            return value * to_meter, 'meter'
        else:
            return value, unit
    elif unit == 'mass':
        to_kg = conversion_factors['mass']['kilogram']
        if unit == 'kilogram':
            return float(value), 'kilogram'
        elif unit == 'gram':
            return value * to_kg, 'kilogram'
        elif unit == 'milligram':
            return value * to_kg, 'kilogram'
        elif unit == 'pound':
            return value * to_kg, 'kilogram'
        elif unit == 'ounce':
            return value * to_kg, 'kilogram'
        else:
            return value, unit
    elif unit == 'volume':
        to_liter = conversion_factors['volume']['liter']
        if unit == 'liter':
            return float(value), 'liter'
        elif unit == 'milliliter':
            return value * to_liter, 'liter'
        elif unit == 'cubic_meter':
            return value * to_liter, 'liter'
        elif unit == 'cubic_centimeter':
            return value * to_liter, 'liter'
        else:
            return value, unit
    return value, unit
if __name__ == '__main__':
    print(convert_to_base(1000, 'kilometer'))
    print(convert_to_base(500, 'gram'))
    print(convert_to_base(120, 'inch'))
    print(convert_to_base(3000, 'milliliter'))
    print(convert_to_base(5, 'pound'))
    print(convert_to_base(2.54, 'meter'))
    print(convert_to_base(10, 'unknown_unit'))