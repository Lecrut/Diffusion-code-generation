def standardize_volume(volumes):
    WATER_CONVERSION = 1.0
    SAND_CONVERSION = 0.001
    GRAVEL_CONVERSION = 0.001

    conversion_factors = {
        'water': WATER_CONVERSION,
        'sand': SAND_CONVERSION,
        'gravel': GRAVEL_CONVERSION
    }

    standardized_volumes = {}
    for substance, volume in volumes.items():
        if substance not in conversion_factors:
            raise ValueError(f'Unsupported substance: {substance}')
        standardized_volume = volume * conversion_factors[substance]
        standardized_volumes[substance] = standardized_volume
    return standardized_volumes

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'gravel': 2000.0}
    print(standardize_volume(sample_volumes))