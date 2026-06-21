def standardize_volume(volumes):
    conversion_factors = {
        'water': 1.0,
        'sand': 0.001,
        'gravel': 0.001
    }
    
    def convert_to_cubic_meters(substance, volume):
        if substance not in conversion_factors:
            raise ValueError(f'Unsupported substance: {substance}')
        return volume * conversion_factors[substance]
    
    standardized_volumes = {}
    for substance, volume in volumes.items():
        try:
            standardized_volume = convert_to_cubic_meters(substance, volume)
            standardized_volumes[substance] = standardized_volume
        except ValueError as e:
            print(e)
    
    return standardized_volumes

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'gravel': 2000.0}
    print(standardize_volume(sample_volumes))