class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'kg_to_lb': 2.20462,
            'lb_to_kg': 1 / 2.20462,
            'kg_to_oz': 35.274,
            'oz_to_kg': 1 / 35.274
        }

    def convert(self, value, from_unit, to_unit):
        factor_key = f'{from_unit}_to_{to_unit}'
        return value * self.conversion_factors[factor_key]

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert(1, 'kg', 'lb'))
    print(converter.convert(2.20462, 'lb', 'kg'))
    print(converter.convert(1, 'kg', 'oz'))
    print(converter.convert(35.274, 'oz', 'kg'))