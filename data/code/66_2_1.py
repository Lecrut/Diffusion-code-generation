class UnitConverter:
    @staticmethod
    def km_to_m(kilometers: float) -> float:
        return kilometers * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.km_to_m(5.5)
    print(result)