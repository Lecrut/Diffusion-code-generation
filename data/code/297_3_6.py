import math
def convert_dimensions(measurements, target_unit):
    conversion_factors = {
        ('m', 'kg'): 0.000625,
        ('ft', 'kg'): 0.0220462,
        ('in', 'kg'): 0.000163871,
        ('lb', 'kg'): 0.453592,
        ('cm', 'kg'): 0.0000220462,
        ('mi', 'kg'): 1609.34,
    }
    results = []
    for value, unit in measurements:
        if unit == target_unit:
            results.append(value)
            continue
        key = (unit, target_unit)
        if key in conversion_factors:
            converted_value = value * conversion_factors[key]
            results.append(converted_value)
        else:
            results.append(f"Error: Conversion factor for {unit} to {target_unit} not found")
    return results
if __name__ == '__main__':
    sample_measurements = [
        (10, 'm'),
        (5, 'lb'),
        (120, 'cm'),
        (1.5, 'ft'),
        (1000, 'mi')
    ]
    target = 'kg'
    converted_values = convert_dimensions(sample_measurements, target)
    print(f"Original measurements: {sample_measurements}")
    print(f"Target unit: {target}")
    print("Converted values:")
    for original, converted in zip(sample_measurements, converted_values):
        if isinstance(converted, float):
            print(f"{original} {sample_measurements[0][1]} -> {converted:.4f} {target}")
        else:
            print(f"{original} {sample_measurements[0][1]} -> {converted}")