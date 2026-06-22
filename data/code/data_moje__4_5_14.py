from enum import Enum
from typing import Union

class DistanceUnit(Enum):
    METER = 'meter'
    KILOMETER = 'kilometer'
    MILE = 'mile'
    YARD = 'yard'
    FOOT = 'foot'
    INCH = 'inch'
    CENTIMETER = 'centimeter'
    MILLIMETER = 'millimeter'
CONVERSION_TO_METERS = {DistanceUnit.METER: 1.0, DistanceUnit.KILOMETER: 1000.0, DistanceUnit.MILE: 1609.344, DistanceUnit.YARD: 0.9144, DistanceUnit.FOOT: 0.3048, DistanceUnit.INCH: 0.0254, DistanceUnit.CENTIMETER: 0.01, DistanceUnit.MILLIMETER: 0.001}

class DistanceConverter:

    def __init__(self):
        self.supported_units = list(DistanceUnit)

    def validate_unit(self, unit: Union[str, DistanceUnit]) -> DistanceUnit:
        if isinstance(unit, DistanceUnit):
            return unit
        if isinstance(unit, str):
            try:
                return DistanceUnit(unit.lower())
            except ValueError:
                raise ValueError(f'Unsupported unit: {unit}. Supported units: {[u.value for u in self.supported_units]}')
        raise TypeError('Unit must be a string or DistanceUnit enum member')

    def convert(self, distance: float, from_unit: Union[str, DistanceUnit], to_unit: Union[str, DistanceUnit]) -> float:
        if not isinstance(distance, (int, float)):
            raise TypeError('Distance must be a number')
        if distance < 0:
            raise ValueError('Distance must be non-negative')
        from_u = self.validate_unit(from_unit)
        to_u = self.validate_unit(to_unit)
        meters = distance * CONVERSION_TO_METERS[from_u]
        result = meters / CONVERSION_TO_METERS[to_u]
        return result
if __name__ == '__main__':
    converter = DistanceConverter()
    result1 = converter.convert(1, 'mile', 'kilometer')
    print(result1)
    result2 = converter.convert(100, 'centimeter', 'inch')
    print(result2)
    result3 = converter.convert(5.5, DistanceUnit.FOOT, DistanceUnit.METER)
    print(result3)
    try:
        converter.convert(-10, 'meter', 'mile')
    except ValueError as e:
        print(str(e))
    try:
        converter.convert(10, 'lightyear', 'meter')
    except ValueError as e:
        print(str(e))