class UnitConverter:
    @staticmethod
    def km_to_m(kilometers: float) -> float:
        return kilometers * 1000.0

if __name__ == '__main__':
    result = UnitConverter.km_to_m(5)
    print(result)