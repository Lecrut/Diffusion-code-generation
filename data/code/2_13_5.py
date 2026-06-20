import math

class VolumeMeasurement:
    CONVERSION_TO_CC = {
        'liters': 1000.0,
        'milliliters': 1.0,
        'gallons': 3785.411784,
        'cubic_meters': 1000000.0,
        'cubic_centimeters': 1.0
    }

    def __init__(self, value, unit='cubic_centimeters'):
        if unit not in self.CONVERSION_TO_CC:
            raise ValueError(f"Unit {unit} is not supported")
        self._base_cc = float(value) * self.CONVERSION_TO_CC[unit]

    @property
    def cubic_centimeters(self):
        return self._base_cc

    def to_liters(self):
        return self._base_cc / self.CONVERSION_TO_CC['liters']

    def to_milliliters(self):
        return self._base_cc / self.CONVERSION_TO_CC['milliliters']

    def to_gallons(self):
        return self._base_cc / self.CONVERSION_TO_CC['gallons']

    def to_cubic_meters(self):
        return self._base_cc / self.CONVERSION_TO_CC['cubic_meters']

    def __add__(self, other):
        if isinstance(other, VolumeMeasurement):
            return VolumeMeasurement(self._base_cc + other._base_cc, 'cubic_centimeters')
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, VolumeMeasurement):
            return VolumeMeasurement(self._base_cc - other._base_cc, 'cubic_centimeters')
        return NotImplemented

    def __mul__(self, scalar):
        return VolumeMeasurement(self._base_cc * float(scalar), 'cubic_centimeters')

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide volume by zero")
        return VolumeMeasurement(self._base_cc / float(scalar), 'cubic_centimeters')

    def __eq__(self, other):
        if not isinstance(other, VolumeMeasurement):
            return False
        return math.isclose(self._base_cc, other._base_cc, rel_tol=1e-9)

    def __repr__(self):
        return f"VolumeMeasurement({self._base_cc} cc)"

if __name__ == '__main__':
    v1 = VolumeMeasurement(1, 'liters')
    v2 = VolumeMeasurement(500, 'milliliters')

    print(v1.to_liters())
    print(v1.to_milliliters())
    print(v1.to_gallons())
    print(v1.to_cubic_meters())

    print(v2.to_liters())
    print(v2.to_milliliters())
    print(v2.to_gallons())
    print(v2.to_cubic_meters())

    v3 = v1 + v2
    print(v3.to_liters())

    v4 = v1 - v2
    print(v4.to_milliliters())

    v5 = v1 * 2
    print(v5.to_liters())

    v6 = v1 / 2
    print(v6.to_milliliters())

    print(v1 == VolumeMeasurement(1000, 'cubic_centimeters'))