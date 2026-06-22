class LengthConverter:
    CONVERSION_FACTORS = {'mm': 1.0, 'cm': 10.0, 'm': 1000.0, 'km': 1000000.0, 'in': 25.4, 'ft': 304.8, 'yd': 914.4}

    def validate_units(self, from_unit, to_unit):
        if from_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f'Unsupported unit: {from_unit}')
        if to_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f'Unsupported unit: {to_unit}')

    def convert(self, value, from_unit, to_unit):
        self.validate_units(from_unit, to_unit)
        value_in_mm = value * self.CONVERSION_FACTORS[from_unit]
        converted_value = value_in_mm / self.CONVERSION_FACTORS[to_unit]
        return converted_value
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1000, 'mm', 'km'))
    print(converter.convert(5, 'km', 'm'))
    print(converter.convert(12, 'in', 'ft'))
    print(converter.convert(3, 'yd', 'cm'))