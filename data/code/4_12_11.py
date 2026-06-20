class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    MILES_TO_METERS = 1609.34
    KILOMETERS_TO_METERS = 1000.0

    def __init__(self, value, from_unit, to_unit):
        self.value = value
        self.from_unit = from_unit.lower()
        self.to_unit = to_unit.lower()

    def _to_meters(self, val, unit):
        if unit == 'miles':
            return val * self.MILES_TO_METERS
        elif unit == 'kilometers':
            return val * self.KILOMETERS_TO_METERS
        elif unit == 'meters':
            return val
        else:
            raise ValueError(f"Unknown unit: {unit}")

    def _from_meters(self, val, unit):
        if unit == 'miles':
            return val / self.MILES_TO_METERS
        elif unit == 'kilometers':
            return val / self.KILOMETERS_TO_METERS
        elif unit == 'meters':
            return val
        else:
            raise ValueError(f"Unknown unit: {unit}")

    def convert(self):
        meters = self._to_meters(self.value, self.from_unit)
        result = self._from_meters(meters, self.to_unit)
        return result

    def get_formatted_result(self):
        result = self.convert()
        return f"{self.value} {self.from_unit} is {result} {self.to_unit}"

if __name__ == '__main__':
    converter1 = DistanceConverter(10, 'miles', 'kilometers')
    print(converter1.convert())
    converter2 = DistanceConverter(5000, 'meters', 'miles')
    print(converter2.convert())
    converter3 = DistanceConverter(1, 'kilometers', 'meters')
    print(converter3.convert())
    print(converter1.get_formatted_result())
    print(converter2.get_formatted_result())
    print(converter3.get_formatted_result())