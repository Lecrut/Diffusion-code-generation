class DistanceConverter:
    KILOMETERS_TO_MILES = 0.621371
    MILES_TO_KILOMETERS = 1 / KILOMETERS_TO_MILES
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / METERS_TO_FEET

    @staticmethod
    def kilometers_to_miles(kilometers: float) -> float:
        return kilometers * DistanceConverter.KILOMETERS_TO_MILES

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        return miles * DistanceConverter.MILES_TO_KILOMETERS

    @staticmethod
    def meters_to_feet(meters: float) -> float:
        return meters * DistanceConverter.METERS_TO_FEET

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        return feet * DistanceConverter.FEET_TO_METERS
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.kilometers_to_miles(1))
    print(converter.miles_to_kilometers(1))
    print(converter.meters_to_feet(1))
    print(converter.feet_to_meters(1))