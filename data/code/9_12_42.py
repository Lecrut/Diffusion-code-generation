class VolumeConversion:
    LITERS_PER_CUBIC_METER = 1000

    @staticmethod
    def convert_cubic_meters_to_liters(cubic_meters):
        if not isinstance(cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        return cubic_meters * VolumeConversion.LITERS_PER_CUBIC_METER

if __name__ == '__main__':
    sample_volume_cubic_meters = 2.75
    converted_volume_liters = VolumeConversion.convert_cubic_meters_to_liters(sample_volume_cubic_meters)
    print(converted_volume_liters)