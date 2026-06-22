import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {
        ('m3', 'ft3'): 35.3147,
        ('ft3', 'm3'): 0.0283168,
        ('l', 'gal'): 0.264172,
        ('gal', 'l'): 3.78541
    }
    
    key = (from_unit, to_unit)
    if key not in conversion_factors:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
    
    factor = conversion_factors[key]
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([10, 20, 30, 40])
    converted_volumes = convert_volumes(sample_volumes, 'm3', 'ft3')
    print(converted_volumes)