class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        if not isinstance(liters, (int, float)):
            raise TypeError("Input must be a number")
        if liters < 0:
            raise ValueError("Input must be non-negative")
        return liters * 1000.0

if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [0, 1, 0.5, 10, 100.75]
    for value in sample_values:
        result = converter.liters_to_milliliters(value)
        print(result)