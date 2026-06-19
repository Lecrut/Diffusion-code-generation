import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {
        ('m3', 'cm3'): 1e6,
        ('cm3', 'm3'): 1e-6,
        ('m3', 'l'): 1000,
        ('l', 'm3'): 0.001,
        ('cm3', 'l'): 0.001,
        ('l', 'cm3'): 1000,
    }
    
    key = (from_unit, to_unit)
    if key not in conversion_factors:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
    
    factor = conversion_factors[key]
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    converted_volumes = convert_volumes(sample_volumes, 'm3', 'cm3')
    print(converted_volumes)