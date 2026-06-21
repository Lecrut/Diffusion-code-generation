class VolumeUnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'cubic_meters': 1000,
            'liters_per_cubic_meter': 1000
        }

    def convert_to_liters(self, cubic_meters):
        if not isinstance(cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        return cubic_meters * self.conversion_factors['cubic_meters']

if __name__ == '__main__':
    sample_volume_cubic_meters = 1.5
    converter = VolumeUnitConverter()
    converted_volume_liters = converter.convert_to_liters(sample_volume_cubic_meters)
    print(converted_volume_liters)