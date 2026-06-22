class UnitConverter:
    KILOMETER_TO_METER_FACTOR = 1000

    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        if kilometers < 0:
            raise ValueError("Kilometers cannot be negative")
        return kilometers * UnitConverter.KILOMETER_TO_METER_FACTOR

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.kilometers_to_meters(3.5))
    print(converter.kilometers_to_meters(0))
    print(converter.kilometers_to_meters(12))