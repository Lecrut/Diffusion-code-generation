from fractions import Fraction

_UNITS = {"feet": Fraction(12), "inch": Fraction(1)}

def convert_units(value, from_unit, to_unit):
    factor = _UNITS[from_unit] / _UNITS[to_unit]
    return value * factor

def feet_to_inches(feet):
    return convert_units(feet, "feet", "inch")

if __name__ == '__main__':
    print(feet_to_inches(5))
    print(feet_to_inches(0))
    print(feet_to_inches(10.5))