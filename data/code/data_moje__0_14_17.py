class LengthConverter:
    METERS = 'm'
    KILOMETERS = 'km'
    CENTIMETERS = 'cm'
    MILLIMETERS = 'mm'
    INCHES = 'in'
    FEET = 'ft'
    YARDS = 'yd'
    MILES = 'mi'

    FACTORS_TO_METERS = {
        METERS: 1.0,
        KILOMETERS: 1000.0,
        CENTIMETERS: 0.01,
        MILLIMETERS: 0.001,
        INCHES: 0.0254,
        FEET: 0.3048,
        YARDS: 0.9144,
        MILES: 1609.344,
    }

    def __init__(self):
        self._cache = {}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.FACTORS_TO_METERS:
            raise ValueError(f"Unsupported from_unit: {from_unit}")
        if to_unit not in self.FACTORS_TO_METERS:
            raise ValueError(f"Unsupported to_unit: {to_unit}")

        cache_key = (from_unit, to_unit)
        if cache_key not in self._cache:
            from_factor = self.FACTORS_TO_METERS[from_unit]
            to_factor = self.FACTORS_TO_METERS[to_unit]
            self._cache[cache_key] = from_factor / to_factor

        return value * self._cache[cache_key]

def convert_length(value, from_unit, to_unit):
    converter = LengthConverter()
    return converter.convert(value, from_unit, to_unit)

if __name__ == '__main__':
    result1 = convert_length(1, LengthConverter.KILOMETERS, LengthConverter.METERS)
    print(result1)

    result2 = convert_length(100, LengthConverter.CENTIMETERS, LengthConverter.INCHES)
    print(result2)

    result3 = convert_length(1, LengthConverter.MILES, LengthConverter.KILOMETERS)
    print(result3)

    result4 = convert_length(5.5, LengthConverter.FEET, LengthConverter.METERS)
    print(result4)

    result5 = convert_length(1, LengthConverter.YARDS, LengthConverter.FEET)
    print(result5)

    result6 = convert_length(25.4, LengthConverter.MILLIMETERS, LengthConverter.INCHES)
    print(result6)

    result7 = convert_length(3.0, LengthConverter.METERS, LengthConverter.YARDS)
    print(result7)

    result8 = convert_length(0.5, LengthConverter.MILES, LengthConverter.FEET)
    print(result8)