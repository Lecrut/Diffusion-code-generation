import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {('m3', 'cm3'): 1000000.0, ('m3', 'liters'): 1000, ('cm3', 'm3'): 1e-06, ('cm3', 'liters'): 1, ('liters', 'm3'): 0.001, ('liters', 'cm3'): 1}
    key = (from_unit, to_unit)
    if key not in conversion_factors:
        raise ValueError('Unsupported unit conversion')
    factor = conversion_factors[key]
    return volumes * factor
if __name__ == '__main__':
    sample_volumes = np.array([10, 20, 30])
    converted_volumes = convert_volumes(sample_volumes, 'm3', 'liters')
    print(converted_volumes)