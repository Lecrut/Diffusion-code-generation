class UnitConverter:
    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        return liters * 1000.0

if __name__ == '__main__':
    converter = UnitConverter()
    sample_liters = 2.5
    result = converter.liters_to_milliliters(sample_liters)
    print(result)
    another_result = UnitConverter.liters_to_milliliters(0.1)
    print(another_result)