class VolumeConversion:
    def __init__(self):
        self.conversion_table = {
            'cubic_meters_to_liters': 1000,
        }

    def convert(self, volume, conversion_type):
        if conversion_type not in self.conversion_table:
            raise ValueError(f"Unsupported conversion type: {conversion_type}")
        return volume * self.conversion_table[conversion_type]

if __name__ == '__main__':
    sample_volume_cubic_meters = 5.0
    converter = VolumeConversion()
    converted_volume_liters = converter.convert(sample_volume_cubic_meters, 'cubic_meters_to_liters')
    print(converted_volume_liters)