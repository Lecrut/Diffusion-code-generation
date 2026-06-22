class VolumeConverter:
    ML_PER_LITER = 1000

    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        return liters * VolumeConverter.ML_PER_LITER

if __name__ == '__main__':
    converter = VolumeConverter()
    result = converter.liters_to_milliliters(2.5)
    print(result)