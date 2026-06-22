class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'water': 1.0,
            'sand': 0.001,
            'gravel': 0.001
        }

    def standardize_volume(self, volumes):
        standardized_volumes = {}
        for substance, volume in volumes.items():
            if substance not in self.conversion_factors:
                raise ValueError(f'Unsupported substance: {substance}')
            standardized_volume = volume * self.conversion_factors[substance]
            standardized_volumes[substance] = standardized_volume
        return standardized_volumes

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'gravel': 2000.0}
    print(converter.standardize_volume(sample_volumes))