import numpy as np

def convert_volumes(volume_array, source_unit='L', target_unit='mL'):
    volume_array = np.asarray(volume_array, dtype=float)
    conversion_factors = {'mL': 1.0, 'L': 1000.0, 'gal': 3785.41, 'qt': 946.35, 'pt': 473.18, 'cup': 236.59, 'fl_oz': 29.57}
    source_factor = conversion_factors.get(source_unit, 1.0)
    target_factor = conversion_factors.get(target_unit, 1.0)
    result = volume_array * (source_factor / target_factor)
    return result
if __name__ == '__main__':
    samples = np.array([1.0, 2.5, 0.5, 10.0, 3.3])
    converted = convert_volumes(samples, source_unit='L', target_unit='mL')
    print(converted)