class DistanceConverter:
    def __init__(self, value, unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        self._value = float(value)
        self._unit = unit.lower()
        if self._unit not in ('meters', 'kilometers', 'miles'):
            raise ValueError("Unit must be meters, kilometers, or miles")

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def to_meters(self):
        if self._unit == 'meters':
            return self._value
        if self._unit == 'kilometers':
            return self._value * 1000.0
        if self._unit == 'miles':
            return self._value * 1609.344

    def to_kilometers(self):
        meters = self.to_meters()
        return meters / 1000.0

    def to_miles(self):
        meters = self.to_meters()
        return meters / 1609.344

    def convert(self, target_unit):
        if target_unit.lower() == 'meters':
            result = self.to_meters()
        elif target_unit.lower() == 'kilometers':
            result = self.to_kilometers()
        elif target_unit.lower() == 'miles':
            result = self.to_miles()
        else:
            raise ValueError("Target unit must be meters, kilometers, or miles")
        return result

    def __str__(self):
        if self._unit == 'meters':
            val = self.to_meters()
            unit_name = 'meters'
        elif self._unit == 'kilometers':
            val = self.to_kilometers()
            unit_name = 'kilometers'
        else:
            val = self.to_miles()
            unit_name = 'miles'
        return f"{val} {unit_name}"

if __name__ == '__main__':
    converter = DistanceConverter(5, 'kilometers')
    meters = converter.to_meters()
    miles = converter.to_miles()
    print(meters)
    print(miles)