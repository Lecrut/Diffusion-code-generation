class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000

    @staticmethod
    def to_milliliters(liters):
        return liters * VolumeConverter.LITERS_TO_MILLILITERS

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.to_milliliters(2.5)
    print(result)