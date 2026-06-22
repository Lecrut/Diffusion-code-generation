class UnitConverter:
    LITERS_TO_MILLILITERS_FACTOR = 1000

    @staticmethod
    def convert_liters_to_milliliters(liters):
        return int(liters) * UnitConverter.LITERS_TO_MILLILITERS_FACTOR

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert_liters_to_milliliters(5)
    print(result)