class UnitConverter:

    def __init__(self, base_unit, conversion_factors):
        self.base_unit = base_unit
        self.conversion_factors = conversion_factors

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f'Unknown source unit: {from_unit}')
        if to_unit not in self.conversion_factors:
            raise ValueError(f'Unknown target unit: {to_unit}')
        base_value = value * self.conversion_factors[from_unit]
        result = base_value / self.conversion_factors[to_unit]
        return result

def create_length_converter():
    factors = {'meter': 1.0, 'kilometer': 1000.0, 'centimeter': 0.01, 'millimeter': 0.001, 'inch': 0.0254, 'foot': 0.3048, 'yard': 0.9144, 'mile': 1609.344}
    return UnitConverter('meter', factors)
if __name__ == '__main__':
    converter = create_length_converter()
    val1 = converter.convert(1, 'mile', 'meter')
    print(val1)
    val2 = converter.convert(100, 'centimeter', 'inch')
    print(val2)
    val3 = converter.convert(5, 'foot', 'kilometer')
    print(val3)
    val4 = converter.convert(0.5, 'kilometer', 'centimeter')
    print(val4)