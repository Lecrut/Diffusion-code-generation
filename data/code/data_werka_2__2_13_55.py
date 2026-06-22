class VolumeConverter:
    MILLILITERS_TO_FLUID_OUNCES = 0.033814

    @staticmethod
    def scale_volume(milliliters):
        if milliliters < 0:
            raise ValueError("Volume cannot be negative")
        return milliliters * VolumeConverter.MILLILITERS_TO_FLUID_OUNCES

if __name__ == '__main__':
    sample_value = 750
    converter = VolumeConverter()
    result = converter.scale_volume(sample_value)
    print(result)