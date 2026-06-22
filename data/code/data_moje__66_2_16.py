class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        conversion_factor = 1000
        meters = kilometers * conversion_factor
        return meters

if __name__ == '__main__':
    converter = UnitConverter()
    sample_distance = 12.5
    result = converter.kilometers_to_meters(sample_distance)
    print(result)
    another_distance = 3.0
    second_result = converter.kilometers_to_meters(another_distance)
    print(second_result)