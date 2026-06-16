import math
def convert_dimensions(measurements, target_unit):
    conversion_factors = {
        ('m', 'kg'): 0.000625,
        ('cm', 'kg'): 0.000625,
        ('mm', 'kg'): 0.000001,
        ('in', 'kg'): 0.00685775,
        ('ft', 'kg'): 0.0264172,
        ('lb', 'kg'): 0.453592,
        ('g', 'kg'): 0.001,
    }
    converted_results = []
    for value, unit in measurements:
        if unit == target_unit:
            converted_value = value
        else:
            key = (unit, target_unit)
            if key in conversion_factors:
                factor = conversion_factors[key]
                converted_value = value * factor
            else:
                raise ValueError(f"Unsupported unit conversion: {unit} to {target_unit}")
        converted_results.append(converted_value)
    return converted_results
if __name__ == '__main__':
    sample_measurements = [
        (10, 'm'),
        (500, 'g'),
        (100, 'lb'),
        (2, 'ft')
    ]
    target = 'kg'
    try:
        results = convert_dimensions(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print("Converted results:")
        for original, converted in zip(sample_measurements, results):
            print(f"{original[0]} {original[1]} -> {converted:.4f} {target}")
    except ValueError as e:
        print(f"Error: {e}")