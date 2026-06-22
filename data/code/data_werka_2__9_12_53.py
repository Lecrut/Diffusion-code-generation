class VolumeConversion:
    LITERS_PER_CUBIC_METER = 1000

    def __init__(self, volume_in_cubic_meters):
        if not isinstance(volume_in_cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        self.volume_in_cubic_meters = volume_in_cubic_meters

    def convert_to_liters(self):
        return self.volume_in_cubic_meters * VolumeConversion.LITERS_PER_CUBIC_METER

if __name__ == '__main__':
    sample_volume_cubic_meters = 2.5
    converter = VolumeConversion(sample_volume_cubic_meters)
    converted_volume_liters = converter.convert_to_liters()
    print(converted_volume_liters)