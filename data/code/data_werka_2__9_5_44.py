import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {
        ('m3', 'cm3'): 1e6,
        ('cm3', 'm3'): 1e-6,
        ('m3', 'l'): 1000,
        ('l', 'm3'): 0.001,
        ('cm3', 'ml'): 1,
        ('ml', 'cm3'): 1,
    }
    
    if (from_unit, to_unit) not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    
    factor = conversion_factors[(from_unit, to_unit)]
    return volumes * factor

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    from_unit = 'm3'
    to_unit = 'cm3'
    
    converted_volumes = convert_volumes(sample_volumes, from_unit, to_unit)
    print(converted_volumes)