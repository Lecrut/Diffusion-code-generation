class VolumeStandardizer:
    CONVERSION_FACTORS = {
        'water': 1.0,
        'sand': 0.001,
        'gravel': 0.001
    }

    @staticmethod
    def standardize_volume(volumes):
        standardized_volumes = {}
        for substance, volume in volumes.items():
            if substance not in VolumeStandardizer.CONVERSION_FACTORS:
                raise ValueError(f'Unsupported substance: {substance}')
            standardized_volume = volume * VolumeStandardizer.CONVERSION_FACTORS[substance]
            standardized_volumes[substance] = standardized_volume
        return standardized_volumes

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5500.0, 'gravel': 2000.0}
    print(VolumeStandardizer.standardize_volume(sample_volumes))