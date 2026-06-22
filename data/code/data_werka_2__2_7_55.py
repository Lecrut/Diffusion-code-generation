class VolumeStandardizer:
    def __init__(self):
        self.conversion_factors = {
            'water': 1.0,
            'sand': 0.001,
            'gravel': 0.001
        }

    def standardize_volume(self, volumes):
        standardized_volumes = {}
        for substance, volume in volumes.items():
            try:
                standardized_volume = self._convert_to_cubic_meters(substance, volume)
                standardized_volumes[substance] = standardized_volume
            except ValueError as e:
                print(e)
        return standardized_volumes

    def _convert_to_cubic_meters(self, substance, volume):
        if substance not in self.conversion_factors:
            raise ValueError(f'Unsupported substance: {substance}')
        return volume * self.conversion_factors[substance]

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'gravel': 2000.0}
    standardizer = VolumeStandardizer()
    print(standardizer.standardize_volume(sample_volumes))