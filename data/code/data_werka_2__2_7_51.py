def standardize_volume(volumes):
    conversion_factors = {'water': 1.0, 'sand': 0.5}
    standardized_volumes = {}
    for item, volume in volumes.items():
        if item not in conversion_factors:
            raise ValueError(f'Unsupported item: {item}')
        standardized_volumes[item] = volume * conversion_factors[item]
    return standardized_volumes
if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5.5}
    standardized = standardize_volume(sample_volumes)
    print(standardized)