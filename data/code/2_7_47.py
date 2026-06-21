def standardize_volume(volumes):
    CONVERSION_FACTORS = {
        'water': 1.0,
        'sand': 0.001,
        'gravel': 0.001,
        'rock': 0.002
    }
    
    def convert_to_cubic_meters(substance, volume):
        if substance not in CONVERSION_FACTORS:
            raise ValueError(f'Unsupported substance: {substance}')
        return volume * CONVERSION_FACTORS[substance]
    
    standardized_volumes = {}
    for substance, volume in volumes.items():
        try:
            standardized_volume = convert_to_cubic_meters(substance, volume)
            standardized_volumes[substance] = standardized_volume
        except ValueError as e:
            print(e)
    return standardized_volumes

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500, 'gravel': 2000, 'rock': 3000}
    print(standardize_volume(sample_volumes))