class UnitConverter:
    @staticmethod
    def liters_to_milliliters(value: float) -> float:
        return value * 1000

if __name__ == '__main__':
    result = UnitConverter.liters_to_milliliters(2.5)
    print(result)