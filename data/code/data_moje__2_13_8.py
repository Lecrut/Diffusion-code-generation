class VolumeMeasurement:

    def __init__(self, value=0, unit='cc'):
        self._value = value
        self._unit = unit.lower()
        self._cc = self._convert_to_cc(self._value, self._unit)

    @staticmethod
    def _convert_to_cc(value, unit):
        if unit == 'cc':
            return value
        elif unit == 'ml':
            return value
        elif unit == 'l':
            return value * 1000.0
        elif unit == 'gal':
            return value * 3785.411784
        elif unit == 'm3':
            return value * 1000000.0
        else:
            raise ValueError(f'Unsupported unit: {unit}')

    @staticmethod
    def _convert_from_cc(cc_value, target_unit):
        target_unit = target_unit.lower()
        if target_unit == 'cc':
            return cc_value
        elif target_unit == 'ml':
            return cc_value
        elif target_unit == 'l':
            return cc_value / 1000.0
        elif target_unit == 'gal':
            return cc_value / 3785.411784
        elif target_unit == 'm3':
            return cc_value / 1000000.0
        else:
            raise ValueError(f'Unsupported target unit: {target_unit}')

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    @property
    def cc(self):
        return self._cc

    @property
    def ml(self):
        return self._convert_from_cc(self._cc, 'ml')

    @property
    def l(self):
        return self._convert_from_cc(self._cc, 'l')

    @property
    def gal(self):
        return self._convert_from_cc(self._cc, 'gal')

    @property
    def m3(self):
        return self._convert_from_cc(self._cc, 'm3')

    def to(self, target_unit):
        return self._convert_from_cc(self._cc, target_unit)

    def __add__(self, other):
        if isinstance(other, VolumeMeasurement):
            return VolumeMeasurement(self._cc + other._cc, 'cc')
        else:
            raise TypeError("Unsupported operand type(s) for +: 'VolumeMeasurement' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, VolumeMeasurement):
            return VolumeMeasurement(self._cc - other._cc, 'cc')
        else:
            raise TypeError("Unsupported operand type(s) for -: 'VolumeMeasurement' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return VolumeMeasurement(self._cc * other, 'cc')
        else:
            raise TypeError("Unsupported operand type(s) for *: 'VolumeMeasurement' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError('Cannot divide volume by zero')
            return VolumeMeasurement(self._cc / other, 'cc')
        else:
            raise TypeError("Unsupported operand type(s) for /: 'VolumeMeasurement' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, VolumeMeasurement):
            return abs(self._cc - other._cc) < 1e-09
        else:
            return False

    def __repr__(self):
        return "VolumeMeasurement({:.6f}, '{}')".format(self._value, self._unit)

    def __str__(self):
        return '{:.6f} {}'.format(self._value, self._unit)
if __name__ == '__main__':
    v1 = VolumeMeasurement(1.5, 'l')
    v2 = VolumeMeasurement(500, 'ml')
    v3 = VolumeMeasurement(1, 'gal')
    v4 = VolumeMeasurement(0.001, 'm3')
    print('v1 in cc:', v1.cc)
    print('v1 in ml:', v1.ml)
    print('v1 in l:', v1.l)
    print('v1 in gal:', v1.gal)
    print('v1 in m3:', v1.m3)
    print('v2 in l:', v2.l)
    print('v2 in gal:', v2.gal)
    print('v3 in l:', v3.l)
    print('v3 in cc:', v3.cc)
    print('v4 in l:', v4.l)
    print('v4 in ml:', v4.ml)
    v_sum = v1 + v2
    print('v1 + v2:', v_sum)
    print('v1 + v2 in l:', v_sum.l)
    v_diff = v3 - v2
    print('v3 - v2:', v_diff)
    print('v3 - v2 in ml:', v_diff.ml)
    v_mul = v1 * 2
    print('v1 * 2:', v_mul)
    print('v1 * 2 in cc:', v_mul.cc)
    v_div = v3 / 2
    print('v3 / 2:', v_div)
    print('v3 / 2 in gal:', v_div.gal)
    print('v1 == v1:', v1 == v1)
    print('v1 == v2:', v1 == v2)
    v5 = VolumeMeasurement(1500, 'ml')
    print('v1 == v5:', v1 == v5)
    v6 = v1.to('m3')
    print('v1 to m3:', v6)