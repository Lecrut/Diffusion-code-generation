import math
def standardize_volume(volumes, conversion_factors):
    standardized_volumes = {}
    for item, volume in volumes.items():
        if item in conversion_factors:
            standardized_volume = volume * conversion_factors[item]
            standardized_volumes[item] = standardized_volume
        else:
            standardized_volumes[item] = volume
    return standardized_volumes
if __name__ == '__main__':
    volume_data = {'water': 10.0, 'sand': 5.5, 'air': 2.0}
    conversion_factors = {
        'water': 0.001,
        'sand': 0.000667,
        'air': 0.001225
    }
    result = standardize_volume(volume_data, conversion_factors)
    print(result)