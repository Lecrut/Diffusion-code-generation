class VolumeConverter:
    LITERS_PER_MILLILITER = 0.001

    @staticmethod
    def convert_milliliters_to_liters(milliliters):
        if milliliters < 0:
            raise ValueError("Negative volume not supported")
        return milliliters * VolumeConverter.LITERS_PER_MILLILITER

if __name__ == '__main__':
    value = 1500
    result = VolumeConverter.convert_milliliters_to_liters(value)
    print(result)