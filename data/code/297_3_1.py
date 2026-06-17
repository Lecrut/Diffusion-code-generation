import math
def convert_dimensions(measurements, target_unit):
    conversion_factors = {
        ('m', 'kg'): 0.000625,
        ('cm', 'kg'): 0.000625,
        ('in', 'lb'): 0.453592,
        ('ft', 'kg'): 0.0277778,
        ('ft', 'lb'): 2.20462,
        ('lb', 'kg'): 0.453592,
    }
    converted_results = []
    for value, unit in measurements:
        if unit == target_unit:
            converted_results.append(value)
            continue
        found = False
        for (from_unit, to_unit), factor in conversion_factors.items():
            if from_unit == unit and to_unit == target_unit:
                result = value * factor
                converted_results.append(result)
                found = True
                break
        if not found:
            raise ValueError(f"Unsupported conversion: {unit} to {target_unit}")
    return converted_results
if __name__ == '__main__':
    sample_measurements = [
        (10, 'm'),
        (50, 'lb'),
        (2, 'ft'),
        (100, 'cm')
    ]
    target = 'kg'
    try:
        results = convert_dimensions(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print("Converted results:")
        for original, converted in zip(sample_measurements, results):
            print(f"{original} {sample_measurements[0][1] if sample_measurements[0][1] == 'm' else sample_measurements[0][1]} -> {converted:.4f} {target}")
    except ValueError as e:
        print(f"Error during conversion: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")