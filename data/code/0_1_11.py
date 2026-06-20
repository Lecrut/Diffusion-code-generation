class UnitConverter:
    METERS_PER_KILOMETER = 1000.0
    FEET_PER_METER = 3.28084

    @staticmethod
    def meters_to_feet(meters):
        return meters * UnitConverter.FEET_PER_METER

    @staticmethod
    def meters_to_kilometers(meters):
        return meters / UnitConverter.METERS_PER_KILOMETER

    @staticmethod
    def feet_to_meters(feet):
        return feet / UnitConverter.FEET_PER_METER

    @staticmethod
    def feet_to_kilometers(feet):
        meters = UnitConverter.feet_to_meters(feet)
        return UnitConverter.meters_to_kilometers(meters)

    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers * UnitConverter.METERS_PER_KILOMETER

    @staticmethod
    def kilometers_to_feet(kilometers):
        meters = UnitConverter.kilometers_to_meters(kilometers)
        return UnitConverter.meters_to_feet(meters)

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.meters_to_feet(100))
    print(converter.kilometers_to_feet(5))
    print(converter.feet_to_meters(328.084))