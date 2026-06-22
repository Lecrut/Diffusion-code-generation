METERS_PER_KILOMETER = 1000

class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        conversion_factor = METERS_PER_KILOMETER
        result = kilometers * conversion_factor
        return result

if __name__ == '__main__':
    converter = UnitConverter()
    sample_distance_km = 3.14159
    converted_meters = converter.kilometers_to_meters(sample_distance_km)
    print(converted_meters)