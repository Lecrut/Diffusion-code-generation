class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        meters = self._to_meters(value, from_unit)
        return self._from_meters(meters, to_unit)

    def _to_meters(self, value, unit):
        if unit == 'm':
            return value
        if unit == 'ft':
            return value / 3.28084
        raise ValueError(f"Unsupported unit: {unit}")

    def _from_meters(self, value, unit):
        if unit == 'm':
            return value
        if unit == 'ft':
            return value * 3.28084
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    result = converter.convert(1, 'm', 'ft')
    print(result)
    result2 = converter.convert(3.28084, 'ft', 'm')
    print(result2)