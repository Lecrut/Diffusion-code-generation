class DistanceConverter:
    METER_TO_KM = 0.001
    METER_TO_MILE = 0.000621371
    KM_TO_METER = 1000.0
    KM_TO_MILE = 0.621371
    MILE_TO_METER = 1609.34
    MILE_TO_KM = 1.60934

    @staticmethod
    def convert_meters_to_kilometers(value: float) -> float:
        return value * DistanceConverter.METER_TO_KM

    @staticmethod
    def convert_meters_to_miles(value: float) -> float:
        return value * DistanceConverter.METER_TO_MILE

    @staticmethod
    def convert_kilometers_to_meters(value: float) -> float:
        return value * DistanceConverter.KM_TO_METER

    @staticmethod
    def convert_kilometers_to_miles(value: float) -> float:
        return value * DistanceConverter.KM_TO_MILE

    @staticmethod
    def convert_miles_to_meters(value: float) -> float:
        return value * DistanceConverter.MILE_TO_METER

    @staticmethod
    def convert_miles_to_kilometers(value: float) -> float:
        return value * DistanceConverter.MILE_TO_KM

if __name__ == '__main__':
    converter = DistanceConverter()
    meters_input = 1000
    km_result = converter.convert_meters_to_kilometers(meters_input)
    miles_result = converter.convert_meters_to_miles(meters_input)
    print(km_result)
    print(miles_result)
    print(converter.convert_kilometers_to_miles(5))
    print(converter.convert_miles_to_kilometers(2))