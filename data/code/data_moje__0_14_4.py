import math

_M_TO_MM = 1000
_MM_TO_IN = 0.03937007874015748
_IN_TO_FT = 1 / 12
_FT_TO_YD = 1 / 3
_YD_TO_MI = 1 / 1760

_M_TO_CM = 100
_M_TO_KM = 0.001
_M_TO_IN = _MM_TO_IN * _M_TO_MM
_M_TO_FT = _M_TO_IN * _IN_TO_FT
_M_TO_YD = _M_TO_FT * _FT_TO_YD
_M_TO_MI = _M_TO_YD * _YD_TO_MI

_IN_TO_M = 1 / _M_TO_IN
_IN_TO_CM = _IN_TO_M * _M_TO_CM
_IN_TO_MM = _IN_TO_M * _M_TO_MM
_IN_TO_FT = _IN_TO_M * _M_TO_FT
_IN_TO_YD = _IN_TO_M * _M_TO_YD
_IN_TO_MI = _IN_TO_M * _M_TO_MI

_FT_TO_M = 1 / _M_TO_FT
_FT_TO_CM = _FT_TO_M * _M_TO_CM
_FT_TO_MM = _FT_TO_M * _M_TO_MM
_FT_TO_IN = 12
_FT_TO_YD = _FT_TO_M * _M_TO_YD
_FT_TO_MI = _FT_TO_M * _M_TO_MI

_YD_TO_M = 1 / _M_TO_YD
_YD_TO_CM = _YD_TO_M * _M_TO_CM
_YD_TO_MM = _YD_TO_M * _M_TO_MM
_YD_TO_IN = 36
_YD_TO_FT = 3
_YD_TO_MI = _YD_TO_M * _M_TO_MI

_MI_TO_M = 1 / _M_TO_MI
_MI_TO_CM = _MI_TO_M * _M_TO_CM
_MI_TO_MM = _MI_TO_M * _M_TO_MM
_MI_TO_IN = 63360
_MI_TO_FT = 5280
_MI_TO_YD = 1760

_CM_TO_M = 1 / 100
_CM_TO_MM = 10
_CM_TO_IN = 1 / _IN_TO_CM
_CM_TO_FT = 1 / _FT_TO_CM
_CM_TO_YD = 1 / _YD_TO_CM
_CM_TO_MI = 1 / _MI_TO_CM

_MM_TO_M = 1 / _M_TO_MM
_MM_TO_CM = 1 / _CM_TO_MM
_MM_TO_IN = 1 / _IN_TO_MM
_MM_TO_FT = 1 / _FT_TO_MM
_MM_TO_YD = 1 / _YD_TO_MM
_MM_TO_MI = 1 / _MI_TO_MM

_UNITS = {
    'm': {
        'm': 1, 'km': 1000, 'cm': _M_TO_CM, 'mm': _M_TO_MM,
        'in': 1 / _M_TO_IN, 'ft': 1 / _M_TO_FT, 'yd': 1 / _M_TO_YD, 'mi': 1 / _M_TO_MI
    },
    'km': {
        'm': 0.001, 'km': 0.001, 'cm': 100, 'mm': 100000,
        'in': 39370.07874015748, 'ft': 3280.839895013123, 'yd': 1093.6132983377078, 'mi': 0.6213711922373341
    },
    'cm': {
        'm': _CM_TO_M, 'km': _CM_TO_M * 0.001, 'cm': 1, 'mm': _CM_TO_MM,
        'in': 1 / _IN_TO_CM, 'ft': 1 / _FT_TO_CM, 'yd': 1 / _YD_TO_CM, 'mi': 1 / _MI_TO_CM
    },
    'mm': {
        'm': _MM_TO_M, 'km': _MM_TO_M * 0.001, 'cm': _MM_TO_CM, 'mm': 1,
        'in': 1 / _IN_TO_MM, 'ft': 1 / _FT_TO_MM, 'yd': 1 / _YD_TO_MM, 'mi': 1 / _MI_TO_MM
    },
    'in': {
        'm': _IN_TO_M, 'km': _IN_TO_M * 0.001, 'cm': _IN_TO_CM, 'mm': _IN_TO_MM,
        'in': 1, 'ft': _IN_TO_FT, 'yd': _IN_TO_YD, 'mi': _IN_TO_MI
    },
    'ft': {
        'm': _FT_TO_M, 'km': _FT_TO_M * 0.001, 'cm': _FT_TO_CM, 'mm': _FT_TO_MM,
        'in': _FT_TO_IN, 'ft': 1, 'yd': _FT_TO_YD, 'mi': _FT_TO_MI
    },
    'yd': {
        'm': _YD_TO_M, 'km': _YD_TO_M * 0.001, 'cm': _YD_TO_CM, 'mm': _YD_TO_MM,
        'in': _YD_TO_IN, 'ft': _YD_TO_FT, 'yd': 1, 'mi': _YD_TO_MI
    },
    'mi': {
        'm': _MI_TO_M, 'km': _MI_TO_M * 0.001, 'cm': _MI_TO_CM, 'mm': _MI_TO_MM,
        'in': _MI_TO_IN, 'ft': _MI_TO_FT, 'yd': _MI_TO_YD, 'mi': 1
    }
}

_STANDARD_UNITS = ('m', 'km', 'cm', 'mm', 'in', 'ft', 'yd', 'mi')

def convert(value, unit_in, unit_out):
    if unit_in not in _STANDARD_UNITS:
        raise ValueError(f"Invalid input unit: {unit_in}")
    if unit_out not in _STANDARD_UNITS:
        raise ValueError(f"Invalid output unit: {unit_out}")
    
    if unit_in == unit_out:
        return value
    
    factors = _UNITS[unit_in]
    return value * factors[unit_out]

def create_converter(initial_unit):
    class LengthConverter:
        def __init__(self, unit):
            self.unit = unit
            self.factors = _UNITS[unit]

        def to(self, target_unit):
            if self.unit == target_unit:
                return self
            self.unit = target_unit
            return self

        def apply(self, value):
            return value * self.factors[self.unit]

    return LengthConverter(initial_unit)

if __name__ == '__main__':
    result = convert(5280, 'ft', 'mi')
    print(result)

    converter = create_converter('in').to('cm')
    print(converter.apply(12))

    print(convert(1, 'mi', 'km'))
    print(convert(100, 'cm', 'in'))