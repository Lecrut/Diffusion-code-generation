class VolumeConversion:
    def __init__(self):
        self._liters_per_cubic_meter = 1000

    def convert(self, cubic_meters):
        if not isinstance(cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        return cubic_meters * self._liters_per_cubic_meter

if __name__ == '__main__':
    converter = VolumeConversion()
    sample_volume_1 = 0.75
    sample_volume_2 = 1.25
    converted_volume_1 = converter.convert(sample_volume_1)
    converted_volume_2 = converter.convert(sample_volume_2)
    print(converted_volume_1)
    print(converted_volume_2)