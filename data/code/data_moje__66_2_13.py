class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        return kilometers * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    sample_km = 5.5
    result = converter.kilometers_to_meters(sample_km)
    print(result)