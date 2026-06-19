def standardize_volume(volumes):
    conversion_factors = {'water': 1.0, 'sand': 0.000595, 'gravel': 0.0007646}
    standardized_volumes = {}
    for item, volume in volumes.items():
        if item in conversion_factors:
            standardized_volumes[item] = volume * conversion_factors[item]
    return standardized_volumes
if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5.5, 'gravel': 3.0}
    print(standardize_volume(sample_volumes))