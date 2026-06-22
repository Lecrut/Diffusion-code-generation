import math

class DistanceConverter:
    METERS_PER_KILOMETER = 1000
    METERS_PER_MILE = 1609.34

    def __init__(self):
        self.supported_units = ['m', 'km', 'mi']

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        if from_unit not in self.supported_units:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_unit not in self.supported_units:
            raise ValueError(f"Invalid target unit: {to_unit}")
        
        value_in_meters = 0
        if from_unit == 'm':
            value_in_meters = value
        elif from_unit == 'km':
            value_in_meters = value * self.METERS_PER_KILOMETER
        elif from_unit == 'mi':
            value_in_meters = value * self.METERS_PER_MILE
        
        if to_unit == 'm':
            return value_in_meters
        elif to_unit == 'km':
            return value_in_meters / self.METERS_PER_KILOMETER
        elif to_unit == 'mi':
            return value_in_meters / self.METERS_PER_MILE

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(5, 'km', 'mi'))
    print(converter.convert(10, 'mi', 'km'))
    print(converter.convert(1609.34, 'm', 'mi'))
    print(converter.convert(2000, 'm', 'km'))
    try:
        converter.convert(-5, 'km', 'mi')
    except ValueError as e:
        print(e)
    try:
        converter.convert(5, 'ft', 'mi')
    except ValueError as e:
        print(e)