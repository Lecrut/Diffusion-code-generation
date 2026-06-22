class UnitConverter:
    _LITER_TO_ML = 1000

    @staticmethod
    def liters_to_milliliters(liters: float) -> float:
        return liters * UnitConverter._LITER_TO_ML

if __name__ == '__main__':
    result = UnitConverter.liters_to_milliliters(2.5)
    print(result)