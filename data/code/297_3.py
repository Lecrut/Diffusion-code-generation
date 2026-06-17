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
        found = False
        for (source_unit, target_unit_val), factor in conversion_factors.items():
            if source_unit == unit and target_unit_val == target_unit:
                converted_value = value * factor
                results.append(converted_value)
                found = True
                break
        if not found:
            raise ValueError(f"Unsupported conversion: {unit} to {target_unit}")
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10.0, 'm'),
        (5.0, 'lb'),
        (200.0, 'cm'),
        (10.0, 'ft')
    ]
    target = 'kg'
    try:
        converted_values = convert_dimensions(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print(f"Converted values: {converted_values}")
    except ValueError as e:
        print(f"Error: {e}")