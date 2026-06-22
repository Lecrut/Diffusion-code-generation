class VolumeConverter:
    _MILLILITERS_PER_LITER = 1000

    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        if not isinstance(liters, (int, float)):
            raise TypeError("Liters must be a numeric type.")
        if liters < 0:
            raise ValueError("Liters cannot be negative.")
        return liters * VolumeConverter._MILLILITERS_PER_LITER

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_liters = 3.75
    result = converter.liters_to_milliliters(sample_liters)
    print(result)
    sample_liters_2 = 0.001
    result_2 = converter.liters_to_milliliters(sample_liters_2)
    print(result_2)