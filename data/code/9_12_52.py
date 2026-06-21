class VolumeConversion:
    CUBIC_METERS_TO_LITERS = 1000

    @staticmethod
    def convert(volume):
        if not isinstance(volume, (int, float)):
            raise ValueError("Volume must be a number")
        return volume * VolumeConversion.CUBIC_METERS_TO_LITERS

if __name__ == '__main__':
    sample_volume_cubic_meters = 2.75
    converted_volume_liters = VolumeConversion.convert(sample_volume_cubic_meters)
    print(converted_volume_liters)