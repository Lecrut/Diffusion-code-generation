def standardize_volume(volumes):
    conversion_factors = {
        'water': 1.0,
        'sand': 0.001,
        'gravel': 0.001,
        'concrete': 0.001
    }
    
    def validate_substance(substance):
        if substance not in conversion_factors:
            raise ValueError(f'Unsupported substance: {substance}')
    
    standardized_volumes = {}
    for substance, volume in volumes.items():
        validate_substance(substance)
        standardized_volume = volume * conversion_factors[substance]
        standardized_volumes[substance] = standardized_volume
    return standardized_volumes

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'gravel': 2000.0, 'concrete': 3000.0}
    print(standardize_volume(sample_volumes))