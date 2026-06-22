class VolumeConversion:
    METERS_TO_LITERS = 1000

    @staticmethod
    def convert_cubic_meters_to_liters(cubic_meters):
        if not isinstance(cubic_meters, (int, float)):
            raise ValueError("Volume must be a number")
        return cubic_meters * VolumeConversion.METERS_TO_LITERS

if __name__ == '__main__':
    sample_volume = 5.0
    converter = VolumeConversion()
    converted_volume = converter.convert_cubic_meters_to_liters(sample_volume)
    print(converted_volume)