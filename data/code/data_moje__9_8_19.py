import numpy as np

def convert_volumes(values, from_unit, to_unit):
    units_to_liters = {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon': 3.785411784,
        'quart': 0.946352946,
        'pint': 0.473176473,
        'cup': 0.2365882365,
        'fluid_ounce': 0.0295735295625,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001,
        'cubic_inch': 0.016387064,
        'cubic_foot': 28.316846592
    }

    if from_unit not in units_to_liters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units_to_liters:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    from_factor = units_to_liters[from_unit]
    to_factor = units_to_liters[to_unit]

    values_array = np.array(values, dtype=float)
    liters = values_array * from_factor
    result = liters / to_factor
    return result

if __name__ == '__main__':
    sample_measurements = [1.0, 5.0, 10.0, 2.5, 100.0]
    source = 'gallon'
    target = 'liter'
    converted_values = convert_volumes(sample_measurements, source, target)
    print(converted_values)