import math
CONVERSION_FACTORS = {
    'km': 0.001,
    'cm': 100.0,
    'mm': 1000.0,
    'inches': 39.3700787402,
}
def convert_length(meters: float) -> dict:
    result = {}
    for unit, factor in CONVERSION_FACTORS.items():
        if unit == 'km' or unit == 'cm' or unit == 'mm':
            value = meters * factor
        else:
            value = meters / 0.0254
        result[unit] = round(value, 6)
    return result
if __name__ == '__main__':
    sample_values = [1.5, -23.75, 0, 9999.8]
    for val in sample_values:
        conversions = convert_length(val)
        print(f"Input ({val} m): {conversions}")