class VolumeConversion:
    def __init__(self):
        self.factor = 1000

    def convert(self, cubic_meters):
        if not isinstance(cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        return cubic_meters * self.factor

if __name__ == '__main__':
    sample_volume_cubic_meters = 2.75
    converter = VolumeConversion()
    converted_volume_liters = converter.convert(sample_volume_cubic_meters)
    print(converted_volume_liters)