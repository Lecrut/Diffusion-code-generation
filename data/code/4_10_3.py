class DistanceConverter:
    MILE_TO_KM = 1.60934
    KM_TO_MILE = 0.621371

    @staticmethod
    def convert_miles_to_kilometers(miles):
        if not isinstance(miles, (int, float)):
            raise ValueError("Input must be a number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * DistanceConverter.MILE_TO_KM

    @staticmethod
    def convert_kilometers_to_miles(kilometers):
        if not isinstance(kilometers, (int, float)):
            raise ValueError("Input must be a number")
        if kilometers < 0:
            raise ValueError("Distance cannot be negative")
        return kilometers * DistanceConverter.KM_TO_MILE

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_input = 10
    km_result = converter.convert_miles_to_kilometers(miles_input)
    print(km_result)
    km_input = 10
    miles_result = converter.convert_kilometers_to_miles(km_input)
    print(miles_result)