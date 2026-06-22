def standardize_volume(volumes, conversion_factors):
    standardized_volumes = {}
    for item, volume in volumes.items():
        if item in conversion_factors:
            standardized_volumes[item] = volume * conversion_factors[item]
        else:
            standardized_volumes[item] = volume
    return standardized_volumes
if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5.5}
    conversion_factors = {'water': 0.001, 'sand': 1e-06}
    standardized = standardize_volume(sample_volumes, conversion_factors)
    print(standardized)