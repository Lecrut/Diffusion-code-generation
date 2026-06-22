class VolumeConverter:
    LITERS_TO_MILLILITERS_FACTOR = 1000

    @staticmethod
    def to_milliliters(liters: int) -> int:
        return liters * VolumeConverter.LITERS_TO_MILLILITERS_FACTOR

if __name__ == '__main__':
    print(VolumeConverter.to_milliliters(2))