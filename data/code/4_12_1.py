class DistanceConverter:
    MILES_TO_METERS = 1609.344
    KILOMETERS_TO_METERS = 1000.0
    METERS_TO_MILES = 1 / MILES_TO_METERS
    METERS_TO_KILOMETERS = 1 / KILOMETERS_TO_METERS

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()
        self._units = {'miles', 'kilometers', 'meters'}

    def _to_meters(self):
        if self.unit == 'miles':
            return self.value * DistanceConverter.MILES_TO_METERS
        elif self.unit == 'kilometers':
            return self.value * DistanceConverter.KILOMETERS_TO_METERS
        elif self.unit == 'meters':
            return self.value
        else:
            raise ValueError("Unsupported unit")

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit not in self._units:
            raise ValueError("Unsupported target unit")
        meters = self._to_meters()
        if target_unit == 'miles':
            return meters * DistanceConverter.METERS_TO_MILES
        elif target_unit == 'kilometers':
            return meters * DistanceConverter.METERS_TO_KILOMETERS
        elif target_unit == 'meters':
            return meters

    def convert(self, value, unit, target_unit):
        converter = DistanceConverter(value, unit)
        return converter.convert_to(target_unit)

if __name__ == '__main__':
    converter = DistanceConverter(5, 'miles')
    result_kilometers = converter.convert_to('kilometers')
    print(result_kilometers)
    result_meters = converter.convert_to('meters')
    print(result_meters)
    direct_conversion = converter.convert(100, 'kilometers', 'miles')
    print(direct_conversion)