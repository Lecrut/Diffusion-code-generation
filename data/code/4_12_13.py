class DistanceConverter:
    MILES_TO_METERS = 1609.34
    KILOMETERS_TO_METERS = 1000

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()

    def _to_meters(self, val, unit):
        if unit == 'miles':
            return val * DistanceConverter.MILES_TO_METERS
        elif unit == 'kilometers':
            return val * DistanceConverter.KILOMETERS_TO_METERS
        elif unit == 'meters':
            return val
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    def _from_meters(self, val_meters, target_unit):
        if target_unit == 'miles':
            return val_meters / DistanceConverter.MILES_TO_METERS
        elif target_unit == 'kilometers':
            return val_meters / DistanceConverter.KILOMETERS_TO_METERS
        elif target_unit == 'meters':
            return val_meters
        else:
            raise ValueError(f"Unsupported unit: {target_unit}")

    def convert(self, target_unit):
        base_value = self._to_meters(self.value, self.unit)
        return self._from_meters(base_value, target_unit.lower())

if __name__ == '__main__':
    converter = DistanceConverter(100, 'kilometers')
    print(converter.convert('miles'))
    print(converter.convert('meters'))
    
    converter_miles = DistanceConverter(5, 'miles')
    print(converter_miles.convert('kilometers'))
    print(converter_miles.convert('meters'))