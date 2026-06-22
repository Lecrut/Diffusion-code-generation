def standardize_volume(volumes):
    conversion_factors = {'water': 1.0, 'sand': 1.5, 'gravel': 2.0}
    standardized_volumes = {item: volumes[item] * conversion_factors.get(item, 1.0) for item in volumes}
    return standardized_volumes
if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5.5, 'gravel': 3.0}
    standardized = standardize_volume(sample_volumes)
    print(standardized)