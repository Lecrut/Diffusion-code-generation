class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        return kilometers * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.kilometers_to_meters(42.5)
    print(result)