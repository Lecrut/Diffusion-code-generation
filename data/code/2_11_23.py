def standardize_volume(volumes):
    conversion_factors = {'water': 1.0, 'sand': 0.001}
    standardized_volumes = {}
    for substance, volume in volumes.items():
        if substance in conversion_factors:
            standardized_volumes[substance] = volume * conversion_factors[substance]
        else:
            raise ValueError(f'No conversion factor available for {substance}')
    return standardized_volumes
if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500}
    standardized = standardize_volume(sample_volumes)
    print(standardized)