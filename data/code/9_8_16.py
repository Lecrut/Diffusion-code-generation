import numpy as np

def convert_volumes(measurements, from_unit, to_unit):
    conversion_factors = {
        ('ml', 'l'): 0.001,
        ('l', 'ml'): 1000,
        ('cup', 'ml'): 236.588,
        ('ml', 'cup'): 1 / 236.588,
        ('gallon', 'l'): 3.78541,
        ('l', 'gallon'): 1 / 3.78541,
        ('quart', 'l'): 0.946353,
        ('l', 'quart'): 1 / 0.946353,
        ('pint', 'ml'): 473.176,
        ('ml', 'pint'): 1 / 473.176,
        ('fl_oz', 'ml'): 29.5735,
        ('ml', 'fl_oz'): 1 / 29.5735,
        ('tbsp', 'ml'): 14.7868,
        ('ml', 'tbsp'): 1 / 14.7868,
        ('tsp', 'ml'): 4.92892,
        ('ml', 'tsp'): 1 / 4.92892,
    }
    if from_unit == to_unit:
        return measurements.copy()
    factor = conversion_factors.get((from_unit, to_unit))
    if factor is None:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")
    return measurements * factor

if __name__ == '__main__':
    sample_measurements = np.array([100.0, 250.0, 500.0, 1000.0, 2.5, 0.5])
    converted = convert_volumes(sample_measurements, 'ml', 'l')
    print(converted)
    converted_cups = convert_volumes(sample_measurements, 'ml', 'cup')
    print(converted_cups)
    converted_gallons = convert_volumes(sample_measurements, 'l', 'gallon')
    print(converted_gallons)