class VolumeConverter:
    LITERS_PER_CUBIC_METER = 1000

    def __init__(self):
        self.conversion_factor = VolumeConverter.LITERS_PER_CUBIC_METER

    def convert_cubic_meters_to_liters(self, cubic_meters):
        if not isinstance(cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        return cubic_meters * self.conversion_factor

if __name__ == '__main__':
    sample_volume_1 = 2.0
    sample_volume_2 = 4.5
    converter = VolumeConverter()
    
    converted_volume_1 = converter.convert_cubic_meters_to_liters(sample_volume_1)
    converted_volume_2 = converter.convert_cubic_meters_to_liters(sample_volume_2)
    
    print(converted_volume_1)
    print(converted_volume_2)