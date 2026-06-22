class DistanceConverter:

    def __init__(self):
        self.conversion_factors = {'km_to_miles': 0.621371, 'miles_to_km': 1.60934}

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        key = f'{from_unit.lower()}_{to_unit.lower()}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Unsupported conversion: {from_unit} to {to_unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, 'km', 'miles'))
    print(converter.convert(50, 'miles', 'km'))
    print(converter.convert(10, 'km', 'km'))