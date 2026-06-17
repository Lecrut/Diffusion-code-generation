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
        return value, "Unsupported Unit"
    if 'length' in conversion_factors[unit]:
        base_unit = 'meter'
        factor = conversion_factors[unit]['meter'] / conversion_factors[unit].get(base_unit, 1.0)
        return value * factor, base_unit
    elif 'mass' in conversion_factors[unit]:
        base_unit = 'kilogram'
        factor = conversion_factors[unit]['kilogram'] / conversion_factors[unit].get(base_unit, 1.0)
        return value * factor, base_unit
    elif 'volume' in conversion_factors[unit]:
        base_unit = 'cubic_meter'
        factor = conversion_factors[unit]['cubic_meter'] / conversion_factors[unit].get(base_unit, 1.0)
        return value * factor, base_unit
    else:
        return value, f"Conversion logic missing for {unit}"
if __name__ == '__main__':
    print("--- Length Conversions ---")
    val1, unit1 = 100, 'centimeter'
    result1, base1 = convert_to_base(val1, unit1)
    print(f"{val1} {unit1} is equal to {result1} {base1}")
    val2, unit2 = 5, 'mile'
    result2, base2 = convert_to_base(val2, unit2)
    print(f"{val2} {unit2} is equal to {result2} {base2}")
    print("\n--- Mass Conversions ---")
    val3, unit3 = 2000, 'gram'
    result3, base3 = convert_to_base(val3, unit3)
    print(f"{val3} {unit3} is equal to {result3} {base3}")
    val4, unit4 = 10, 'pound'
    result4, base4 = convert_to_base(val4, unit4)
    print(f"{val4} {unit4} is equal to {result4} {base4}")
    print("\n--- Volume Conversions ---")
    val5, unit5 = 2, 'liter'
    result5, base5 = convert_to_base(val5, unit5)
    print(f"{val5} {unit5} is equal to {result5} {base5}")
    val6, unit6 = 1000000, 'cubic_centimeter'
    result6, base6 = convert_to_base(val6, unit6)
    print(f"{val6} {unit6} is equal to {result6} {base6}")
    print("\n--- Unsupported Unit Test ---")
    val7, unit7 = 10, 'furlong'
    result7, base7 = convert_to_base(val7, unit7)
    print(f"{val7} {unit7} is equal to {result7} {base7}")