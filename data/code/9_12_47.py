class VolumeConversion:
    LITERS_PER_CUBIC_METER = 1000

    @staticmethod
    def validate_volume(volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number")
        if volume < 0:
            raise ValueError("Volume cannot be negative")

    @classmethod
    def convert_cubic_meters_to_liters(cls, cubic_meters):
        cls.validate_volume(cubic_meters)
        return cubic_meters * cls.LITERS_PER_CUBIC_METER

if __name__ == '__main__':
    sample_volumes = [0.5, 1.2, 3.7]
    for volume in sample_volumes:
        try:
            converted_volume = VolumeConversion.convert_cubic_meters_to_liters(volume)
            print(f"{volume} cubic meters is {converted_volume} liters")
        except ValueError as e:
            print(e)