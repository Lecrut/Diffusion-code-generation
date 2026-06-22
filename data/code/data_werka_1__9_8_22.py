import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {
        ('m3', 'cm3'): 1e6,
        ('cm3', 'm3'): 1e-6,
        ('m3', 'liters'): 1000,
        ('liters', 'm3'): 0.001,
        ('cm3', 'liters'): 1,
        ('liters', 'cm3'): 1
    }
    
    key = (from_unit, to_unit)
    if key not in conversion_factors:
        raise ValueError("Unsupported unit conversion")
    
    factor = conversion_factors[key]
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    from_unit = 'm3'
    to_unit = 'liters'
    converted_volumes = convert_volumes(sample_volumes, from_unit, to_unit)
    print(converted_volumes)