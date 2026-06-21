import numpy as np

def convert_volumes_volumes(input_array, from_unit, to_unit):
    conversions = {
        ('ml', 'ml'): 1.0,
        ('ml', 'l'): 0.001,
        ('ml', 'gal'): 0.000264172,
        ('l', 'ml'): 1000.0,
        ('l', 'l'): 1.0,
        ('l', 'gal'): 0.264172,
        ('gal', 'ml'): 3785.41,
        ('gal', 'l'): 3.78541,
        ('gal', 'gal'): 1.0,
    }
    key = (from_unit.lower(), to_unit.lower())
    if key not in conversions:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    factor = conversions[key]
    return input_array * factor

if __name__ == '__main__':
    measurements = np.array([100, 250, 500, 1000, 2500])
    converted = convert_volumes_volumes(measurements, 'ml', 'l')
    print(converted)