def standardize_volume(volumes):
    CONVERSION_FACTORS = {
        'water': 1.0,
        'sand': 0.001,
        'gravel': 0.001
    }
    
    standardized_volumes = {}
    
    for substance, volume in volumes.items():
        if substance not in CONVERSION_FACTORS:
            raise ValueError(f'Unsupported substance: {substance}')
        
        try:
            standardized_volume = volume * CONVERSION_FACTORS[substance]
            standardized_volumes[substance] = standardized_volume
        except TypeError as e:
            print(f'TypeError encountered for {substance}: {e}')
    
    return standardized_volumes

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'gravel': 2000.0}
    print(standardize_volume(sample_volumes))