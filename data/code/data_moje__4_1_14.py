class DistanceConverter:
    def __init__(self):
        self._meters = 0.0

    def set_meters(self, meters):
        if not isinstance(meters, (int, float)):
            raise TypeError("Value must be a number")
        if meters < 0:
            raise ValueError("Distance cannot be negative")
        self._meters = float(meters)

    def get_meters(self):
        return self._meters

    def get_kilometers(self):
        return self._meters / 1000.0

    def get_miles(self):
        return self._meters * 0.000621371

    def set_kilometers(self, kilometers):
        if not isinstance(kilometers, (int, float)):
            raise TypeError("Value must be a number")
        if kilometers < 0:
            raise ValueError("Distance cannot be negative")
        self._meters = float(kilometers) * 1000.0

    def set_miles(self, miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Value must be a number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        self._meters = float(miles) / 0.000621371

    def convert_to(self, unit):
        unit = unit.lower()
        if unit == 'meters':
            return self.get_meters()
        elif unit == 'kilometers':
            return self.get_kilometers()
        elif unit == 'miles':
            return self.get_miles()
        else:
            raise ValueError("Unsupported unit. Use 'meters', 'kilometers', or 'miles'.")

if __name__ == '__main__':
    converter = DistanceConverter()

    converter.set_meters(1000)
    print(converter.get_meters())
    print(converter.get_kilometers())
    print(converter.get_miles())

    converter.set_kilometers(5)
    print(converter.get_meters())
    print(converter.get_kilometers())
    print(converter.get_miles())

    converter.set_miles(1)
    print(converter.get_meters())
    print(converter.get_kilometers())
    print(converter.get_miles())

    print(converter.convert_to('meters'))
    print(converter.convert_to('kilometers'))
    print(converter.convert_to('miles'))