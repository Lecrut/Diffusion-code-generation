import numpy as np

def convert_volumes(volumes, from_unit, to_unit):
    conversion_factors = {('m3', 'ft3'): 35.3147, ('ft3', 'm3'): 0.0283168, ('m3', 'l'): 1000, ('l', 'm3'): 0.001, ('ft3', 'l'): 28.3168, ('l', 'ft3'): 0.0353147}
    key = (from_unit, to_unit)
    if key not in conversion_factors:
        raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
    factor = conversion_factors[key]
    return volumes * factor
if __name__ == '__main__':
    sample_volumes = np.array([100, 200, 300])
    from_unit = 'm3'
    to_unit = 'ft3'
    converted_volumes = convert_volumes(sample_volumes, from_unit, to_unit)
    print(converted_volumes)