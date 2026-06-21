class VolumeConversion:
    LITERS_PER_CUBIC_METER = 1000

    @staticmethod
    def validate_input(volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number")

    @classmethod
    def convert_cubic_meters_to_liters(cls, cubic_meters):
        cls.validate_input(cubic_meters)
        return cubic_meters * cls.LITERS_PER_CUBIC_METER

if __name__ == '__main__':
    sample_volume_cubic_meters = 5.0
    converted_volume_liters = VolumeConversion.convert_cubic_meters_to_liters(sample_volume_cubic_meters)
    print(converted_volume_liters)