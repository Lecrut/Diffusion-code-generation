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
            try:
                if unit == 'm' and target_unit == 'kg':
                    converted_value = value
                elif unit == 'lb' and target_unit == 'kg':
                    converted_value = value * 0.453592
                else:
                    raise ValueError("Unsupported conversion")
                results.append(converted_value)
            except Exception:
                results.append(f"Error converting {value} {unit}")
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
    converted_values = convert_dimensions(sample_measurements, target)
    print(f"Original measurements: {sample_measurements}")
    print(f"Target unit: {target}")
    print(f"Converted measurements to {target}: {converted_values}")