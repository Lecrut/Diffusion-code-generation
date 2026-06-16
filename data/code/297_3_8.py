import math
def convert_dimensions(measurements, target_unit):
    conversion_factors = {
        ('m', 'kg'): 0.000625,
        ('cm', 'kg'): 0.000625,
        ('in', 'kg'): 0.00685775,
        ('ft', 'kg'): 0.0264172,
        ('lb', 'kg'): 0.453592,
        ('g', 'kg'): 0.001
    }
    results = []
    for value, unit in measurements:
        if unit == target_unit:
            results.append(value)
            continue
        key = (unit, target_unit)
        if key in conversion_factors:
            factor = conversion_factors[key]
            converted_value = value * factor
            results.append(converted_value)
        else:
            raise ValueError(f"Unsupported unit conversion: {unit} to {target_unit}")
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, 'm'),
        (5, 'lb'),
        (200, 'cm'),
        (100, 'in'),
        (500, 'g')
    ]
    target = 'kg'
    try:
        converted_values = convert_dimensions(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print(f"Converted values in {target}: {converted_values}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")