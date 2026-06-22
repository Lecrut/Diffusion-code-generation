class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000

    @staticmethod
    def liters_to_milliliters(liters):
        if not isinstance(liters, (int, float)):
            raise TypeError("Input must be a number")
        if liters < 0:
            raise ValueError("Input must be non-negative")
        return liters * VolumeConverter.LITERS_TO_MILLILITERS

if __name__ == '__main__':
    converter = VolumeConverter()
    print(converter.liters_to_milliliters(1))
    print(converter.liters_to_milliliters(2.5))
    print(converter.liters_to_milliliters(0))
    print(converter.liters_to_milliliters(10))