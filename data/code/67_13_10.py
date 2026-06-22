class VolumeConverter:
    _ML_PER_LITER = 1000.0

    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        if not isinstance(liters, (int, float)):
            raise TypeError("Input must be a numeric value representing liters")
        if liters < 0:
            raise ValueError("Volume cannot be negative")
        return float(liters) * VolumeConverter._ML_PER_LITER

if __name__ == '__main__':
    converter = VolumeConverter()
    test_values = [0.001, 12.345, 0]
    for val in test_values:
        print(converter.liters_to_milliliters(val))