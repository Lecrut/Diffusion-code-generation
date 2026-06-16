import math
def convert_to_base(value, unit):
    conversions = {
        'length': {'meter': 1, 'kilometer': 1000, 'centimeter': 0.01, 'millimeter': 0.001},
        'mass': {'kilogram': 1, 'gram': 0.001, 'milligram': 0.000001},
        'volume': {'liter': 0.001, 'cubic_meter': 1, 'cubic_centimeter': 0.000001}
    }
    if unit in conversions:
        base_unit = None
        for base, factor in conversions[unit].items():
            if factor == 1:
                base_unit = base
                break
        if base_unit:
            return value * factor
        else:
            return value
    else:
        return value
if __name__ == '__main__':
    print(f"Length conversion: 2.5 kilometers to meters: {convert_to_base(2.5, 'kilometer')}")
    print(f"Length conversion: 150 centimeters to meters: {convert_to_base(150, 'centimeter')}")
    print(f"Mass conversion: 500 grams to kilograms: {convert_to_base(500, 'gram')}")
    print(f"Volume conversion: 2 cubic meters to liters: {convert_to_base(2, 'cubic_meter')}")
    print(f"Volume conversion: 1000000 cubic centimeters to cubic meters: {convert_to_base(1000000, 'cubic_centimeter')}")
    print(f"Unknown unit conversion (should return original value): 10 dollars to meters: {convert_to_base(10, 'dollar')}")