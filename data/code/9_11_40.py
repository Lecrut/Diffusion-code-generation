class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000

    def __init__(self, volume_in_liters):
        if not isinstance(volume_in_liters, (int, float)):
            raise ValueError("Volume must be a number")
        self.volume_in_liters = volume_in_liters

    def convert_to_milliliters(self):
        return self.volume_in_liters * self.LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_liters = 7.8
    converter = VolumeConverter(sample_liters)
    milliliters = converter.convert_to_milliliters()
    print(milliliters)