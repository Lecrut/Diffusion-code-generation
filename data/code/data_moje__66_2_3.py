class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        return kilometers * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kilometers_to_meters(1.5))
    print(converter.kilometers_to_meters(0))
    print(converter.kilometers_to_meters(10))