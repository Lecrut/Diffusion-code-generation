class UnitConverter:
    LITERS_TO_MILLILITERS = 1000

    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        return liters * UnitConverter.LITERS_TO_MILLILITERS

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.liters_to_milliliters(2.5)
    print(result)