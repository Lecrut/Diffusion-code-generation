class VolumeConverter:
    LITERS_TO_MILLILITERS = 1000.0

    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        if not isinstance(liters, (int, float)):
            raise TypeError("Input must be a number")
        return liters * VolumeConverter.LITERS_TO_MILLILITERS

if __name__ == '__main__':
    converter = VolumeConverter()
    result_1 = converter.liters_to_milliliters(1)
    print(result_1)
    result_2 = converter.liters_to_milliliters(2.5)
    print(result_2)
    result_3 = VolumeConverter.liters_to_milliliters(0)
    print(result_3)