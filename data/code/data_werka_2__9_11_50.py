class VolumeUnitConverter:
    LITERS_TO_MILLILITERS = 1000

    @staticmethod
    def convert_liters_to_milliliters(liters):
        if not isinstance(liters, (int, float)):
            raise ValueError("Volume must be a number")
        return liters * VolumeUnitConverter.LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_liters = 4.5
    milliliters = VolumeUnitConverter.convert_liters_to_milliliters(sample_liters)
    print(milliliters)