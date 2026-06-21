import numpy as np

def convert_volumes(volumes_cm3, target_unit):
    units_to_cm3 = {
        'cm3': 1.0,
        'm3': 1e6,
        'L': 1e3,
        'mL': 1.0,
        'gal': 3785.411784,
        'qt': 946.352946,
        'pt': 473.176473,
        'cup': 236.5882365,
        'fl_oz': 29.5735295625,
        'tbsp': 14.78676478125,
        'tsp': 4.92892159375
    }
    
    if target_unit not in units_to_cm3:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    factor = units_to_cm3[target_unit]
    result = volumes_cm3 / factor
    return result

if __name__ == '__main__':
    measurements = np.array([1000.0, 500.0, 250.0, 100.0])
    converted = convert_volumes(measurements, 'L')
    print(converted)