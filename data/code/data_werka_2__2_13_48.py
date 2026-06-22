class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'milliliters_to_fluid_ounces': 0.033814
        }

    def convert(self, volume, conversion_key):
        if conversion_key not in self.conversion_factors:
            raise ValueError("Unsupported conversion key")
        if volume < 0:
            raise ValueError("Volume cannot be negative")
        return volume * self.conversion_factors[conversion_key]

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_value = 1500
    result = converter.convert(sample_value, 'milliliters_to_fluid_ounces')
    print(result)