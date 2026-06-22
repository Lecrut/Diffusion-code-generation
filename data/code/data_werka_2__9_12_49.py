class VolumeConversion:
    def __init__(self):
        self.conversion_factor = 1000

    def convert(self, volume_cubic_meters):
        if not isinstance(volume_cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        return volume_cubic_meters * self.conversion_factor

if __name__ == '__main__':
    sample_volume = 5.0
    converter = VolumeConversion()
    converted_volume = converter.convert(sample_volume)
    print(converted_volume)