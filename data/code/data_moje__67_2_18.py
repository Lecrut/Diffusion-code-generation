class UnitConverter:
    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        return liters * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    sample_liters = 2.5
    result = converter.liters_to_milliliters(sample_liters)
    print(result)