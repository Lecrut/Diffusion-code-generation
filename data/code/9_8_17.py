import numpy as np

def convert_volumes(values, from_unit, to_unit):
    units = {
        'milliliter': 1e-3,
        'liter': 1,
        'cubic_meter': 1e3,
        'teaspoon': 4.92892e-3,
        'tablespoon': 1.47868e-2,
        'fluid_ounce': 2.95735e-2,
        'cup': 2.36588e-1,
        'pint': 4.73176e-1,
        'quart': 9.46353e-1,
        'gallon': 3.78541,
        'cubic_inch': 1.63871e-2,
        'cubic_foot': 2.83168e1
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit provided")

    values_array = np.asarray(values, dtype=float)
    from_factor = units[from_unit]
    to_factor = units[to_unit]
    
    liters = values_array * from_factor
    result = liters / to_factor
    
    return result

if __name__ == '__main__':
    sample_values = np.array([1.0, 10.0, 100.0, 500.0])
    converted = convert_volumes(sample_values, 'liter', 'gallon')
    print(converted)