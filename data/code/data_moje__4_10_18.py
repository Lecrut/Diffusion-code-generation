class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self):
        self.conversion_factor_miles_to_km = self.MILES_TO_KILOMETERS
        self.conversion_factor_km_to_miles = self.KILOMETERS_TO_MILES

    def miles_to_kilometers(self, miles):
        if not isinstance(miles, (int, float)):
            raise ValueError("Input must be a numeric value")
        return miles * self.conversion_factor_miles_to_km

    def kilometers_to_miles(self, kilometers):
        if not isinstance(kilometers, (int, float)):
            raise ValueError("Input must be a numeric value")
        return kilometers * self.conversion_factor_km_to_miles

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a numeric value")
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit == 'miles' and to_unit == 'kilometers':
            return self.miles_to_kilometers(value)
        elif from_unit == 'kilometers' and to_unit == 'miles':
            return self.kilometers_to_miles(value)
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported conversion units. Use 'miles' and 'kilometers'.")

if __name__ == '__main__':
    converter = DistanceConverter()

    sample_miles = 10.0
    sample_km = 16.0934

    result_km = converter.miles_to_kilometers(sample_miles)
    print(result_km)

    result_miles = converter.kilometers_to_miles(sample_km)
    print(result_miles)

    result_convert = converter.convert(sample_miles, 'miles', 'kilometers')
    print(result_convert)

    result_convert_back = converter.convert(result_km, 'kilometers', 'miles')
    print(result_convert_back)

    try:
        converter.miles_to_kilometers("invalid")
    except ValueError as e:
        print(str(e))

    try:
        converter.convert(10, 'meters', 'feet')
    except ValueError as e:
        print(str(e))