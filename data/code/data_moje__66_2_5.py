class UnitConverter:
    @staticmethod
    def km_to_m(kilometers: float) -> float:
        return kilometers * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    sample_kilometers = 5.5
    result = converter.km_to_m(sample_kilometers)
    print(result)