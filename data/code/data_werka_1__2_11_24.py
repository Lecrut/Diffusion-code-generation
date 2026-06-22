def standardize_volume(volumes):
    conversion_factors = {'water': 1.0, 'sand': 0.001, 'oil': 1e-06}
    standardized_volumes = {}
    for item, volume in volumes.items():
        if item in conversion_factors:
            standardized_volumes[item] = volume * conversion_factors[item]
        else:
            raise ValueError(f'No conversion factor available for {item}')
    return standardized_volumes
if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'oil': 2000000.0}
    standardized = standardize_volume(sample_volumes)
    print(standardized)