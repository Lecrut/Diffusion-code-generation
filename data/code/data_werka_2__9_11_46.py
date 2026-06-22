class VolumeUtils:
    LITERS_TO_MILLILITERS = 1000

    @staticmethod
    def liters_to_milliliters(liters):
        if not isinstance(liters, (int, float)):
            raise ValueError("Volume must be a number")
        return liters * VolumeUtils.LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_liters = 4.3
    milliliters = VolumeUtils.liters_to_milliliters(sample_liters)
    print(milliliters)