def standardize_volume(measurements):
    conversion_factors = {'water': 0.001, 'sand': 0.0005}
    standardized_measurements = {}
    for item, volume in measurements.items():
        if item in conversion_factors:
            standardized_volume = volume * conversion_factors[item]
            standardized_measurements[item] = standardized_volume
    return standardized_measurements
if __name__ == '__main__':
    sample_measurements = {'water': 10.0, 'sand': 5.5}
    standardized = standardize_volume(sample_measurements)
    print(standardized)