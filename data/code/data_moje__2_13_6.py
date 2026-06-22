class VolumeMeasurement:
    def __init__(self, value, unit='cm3'):
        self.value = float(value)
        self.unit = unit.lower()
        self.cm3 = self._to_cm3(self.value, self.unit)

    def _to_cm3(self, value, unit):
        conversions = {
            'cm3': 1.0,
            'mm3': 0.001,
            'm3': 1000000.0,
            'l': 1000.0,
            'ml': 1.0,
            'gal': 3785.411784,
            'ft3': 28316.846592,
            'in3': 16.387064,
            'pt': 473.176473,
            'qt': 946.352946,
            'cup': 236.5882365,
            'floz': 29.5735295625
        }
        factor = conversions.get(unit, 1.0)
        return value * factor

    def to_cm3(self):
        return self.cm3

    def to_mm3(self):
        return self.cm3 * 0.001

    def to_m3(self):
        return self.cm3 * 1e-6

    def to_l(self):
        return self.cm3 * 0.001

    def to_ml(self):
        return self.cm3

    def to_gal(self):
        return self.cm3 / 3785.411784

    def to_ft3(self):
        return self.cm3 / 28316.846592

    def to_in3(self):
        return self.cm3 / 16.387064

    def to_pt(self):
        return self.cm3 / 473.176473

    def to_qt(self):
        return self.cm3 / 946.352946

    def to_cup(self):
        return self.cm3 / 236.5882365

    def to_floz(self):
        return self.cm3 / 29.5735295625

    def to(self, unit):
        if unit == 'cm3':
            return self.to_cm3()
        if unit == 'mm3':
            return self.to_mm3()
        if unit == 'm3':
            return self.to_m3()
        if unit == 'l':
            return self.to_l()
        if unit == 'ml':
            return self.to_ml()
        if unit == 'gal':
            return self.to_gal()
        if unit == 'ft3':
            return self.to_ft3()
        if unit == 'in3':
            return self.to_in3()
        if unit == 'pt':
            return self.to_pt()
        if unit == 'qt':
            return self.to_qt()
        if unit == 'cup':
            return self.to_cup()
        if unit == 'floz':
            return self.to_floz()
        raise ValueError(f"Unsupported unit: {unit}")

    def _convert(self, value):
        return value

    def add(self, other):
        total_cm3 = self.cm3 + other.cm3
        return VolumeMeasurement(total_cm3, 'cm3')

    def subtract(self, other):
        diff_cm3 = self.cm3 - other.cm3
        return VolumeMeasurement(diff_cm3, 'cm3')

    def multiply(self, scalar):
        new_cm3 = self.cm3 * float(scalar)
        return VolumeMeasurement(new_cm3, 'cm3')

    def divide(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        new_cm3 = self.cm3 / float(scalar)
        return VolumeMeasurement(new_cm3, 'cm3')

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, scalar):
        return self.multiply(scalar)

    def __div__(self, scalar):
        return self.divide(scalar)

    def __truediv__(self, scalar):
        return self.divide(scalar)

    def __eq__(self, other):
        if not isinstance(other, VolumeMeasurement):
            return False
        return abs(self.cm3 - other.cm3) < 1e-9

    def __lt__(self, other):
        return self.cm3 < other.cm3

    def __le__(self, other):
        return self.cm3 <= other.cm3

    def __gt__(self, other):
        return self.cm3 > other.cm3

    def __ge__(self, other):
        return self.cm3 >= other.cm3

    def __repr__(self):
        return f"VolumeMeasurement({self.cm3}, 'cm3')"

if __name__ == '__main__':
    vol1 = VolumeMeasurement(1, 'l')
    vol2 = VolumeMeasurement(500, 'ml')
    result = vol1.add(vol2)
    print(result.to_l())
    vol3 = VolumeMeasurement(1, 'gal')
    print(vol3.to_cm3())
    vol4 = VolumeMeasurement(1000, 'cm3')
    print(vol4.to_m3())
    vol5 = vol3.multiply(2)
    print(vol5.to_l())
    print(vol1 == vol4)