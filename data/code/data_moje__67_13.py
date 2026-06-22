class UnitConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000.0

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.liters_to_milliliters(1.5)
    print(result)