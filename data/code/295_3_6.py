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
            'cubic_meter': 1.0,
            'liter': 0.001,
            'milliliter': 0.001,
            'cubic_centimeter': 0.000001
        }
    }
    if unit in conversion_factors:
        if 'length' in conversion_factors[unit]:
            return value * conversion_factors[unit]['meter']
        elif 'mass' in conversion_factors[unit]:
            return value * conversion_factors[unit]['kilogram']
        elif 'volume' in conversion_factors[unit]:
            return value * conversion_factors[unit]['cubic_meter']
    return value
if __name__ == '__main__':
    print(f"10 kilometers to meters: {convert_to_base(10, 'kilometer')}")
    print(f"500 centimeters to meters: {convert_to_base(500, 'centimeter')}")
    print(f"1000000 grams to kilograms: {convert_to_base(1000000, 'gram')}")
    print(f"2 pounds to kilograms: {convert_to_base(2, 'pound')}")
    print(f"5 liters to cubic meters: {convert_to_base(5, 'liter')}")
    print(f"1 cubic centimeter to cubic meters: {convert_to_base(1, 'cubic_centimeter')}")