class VolumeConverter:
    MILLILITERS_TO_FLUID_OUNCES = 0.033814

    @staticmethod
    def convert_milliliters_to_fluid_ounces(milliliters):
        if milliliters < 0:
            raise ValueError("Volume cannot be negative")
        return milliliters * VolumeConverter.MILLILITERS_TO_FLUID_OUNCES

if __name__ == '__main__':
    sample_value = 250
    converter = VolumeConverter()
    result = converter.convert_milliliters_to_fluid_ounces(sample_value)
    print(result)