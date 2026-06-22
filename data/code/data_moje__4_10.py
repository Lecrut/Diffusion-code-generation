class DistanceConverter:
    MILES_TO_KM = 1.60934
    KM_TO_MILES = 1 / MILES_TO_KM

    @staticmethod
    def convert(value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit == to_unit:
            return value
        if from_unit == 'miles' and to_unit == 'kilometers':
            return value * DistanceConverter.MILES_TO_KM
        if from_unit == 'kilometers' and to_unit == 'miles':
            return value * DistanceConverter.KM_TO_MILES
        raise ValueError("Unsupported units. Use 'miles' or 'kilometers'")

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(16.0934, 'kilometers', 'miles'))
    print(converter.convert(0, 'miles', 'kilometers'))
    print(converter.convert(-5, 'kilometers', 'miles'))