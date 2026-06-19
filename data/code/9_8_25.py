import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {
        ('m^3', 'l'): 1000,
        ('l', 'ml'): 1000,
        ('ft^3', 'in^3'): 1728,
        ('in^3', 'cm^3'): 16.3871,
        ('cm^3', 'm^3'): 1e-6
    }
    
    key = (from_unit, to_unit)
    if key in conversion_factors:
        return volumes * conversion_factors[key]
    else:
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_volumes = np.array([1.0, 2.5, 3.75])
    from_unit = 'm^3'
    to_unit = 'l'
    
    converted_volumes = convert_volumes(sample_volumes, from_unit, to_unit)
    print(converted_volumes)