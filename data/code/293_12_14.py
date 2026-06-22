class DistanceConverter:

    def __init__(self):
        self.conversion_factors = {'km_to_m': 1000, 'm_to_km': 1 / 1000, 'mi_to_km': 1.60934, 'km_to_mi': 1 / 1.60934, 'ft_to_km': 0.0003048, 'km_to_ft': 1 / 0.0003048}

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if f'{from_unit}_to_{to_unit}' in self.conversion_factors:
            return value * self.conversion_factors[f'{from_unit}_to_{to_unit}']
        else:
            raise ValueError('Invalid conversion units')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, 'km', 'm'))
    print(converter.convert(5000, 'm', 'km'))
    print(converter.convert(1, 'mi', 'km'))
    print(converter.convert(2.5, 'km', 'mi'))
    print(converter.convert(1000, 'ft', 'km'))
    print(converter.convert(1, 'km', 'ft'))