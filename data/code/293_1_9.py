class DistanceConverter:

    def __init__(self):
        self.conversion_factors = {'km_to_mile': 0.621371, 'mile_to_km': 1.60934}

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        key = f'{from_unit.lower()}_to_{to_unit.lower()}'
        if key not in self.conversion_factors:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
        return value * self.conversion_factors[key]
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'km', 'mile'))
    print(converter.convert(5, 'mile', 'km'))