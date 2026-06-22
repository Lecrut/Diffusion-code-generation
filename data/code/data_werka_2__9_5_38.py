import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {
        'm3_to_cm3': 1e6,
        'cm3_to_m3': 1e-6,
        'm3_to_liters': 1000,
        'liters_to_m3': 0.001,
        'cm3_to_liters': 1,
        'liters_to_cm3': 1
    }
    
    key = f"{from_unit}_to_{to_unit}"
    if key not in conversion_factors:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    
    return volumes * conversion_factors[key]

if __name__ == '__main__':
    sample_volumes = np.array([1, 2.5, 3.75])
    converted_volumes = convert_volumes(sample_volumes, 'm3', 'cm3')
    print(converted_volumes)