class UnitConverter:
    def __init__(self):
        self.base_units = {}
        self.conversion_factors = {}

    def add_unit(self, unit_name, factor_to_base):
        self.base_units[unit_name] = factor_to_base
        self.conversion_factors[unit_name] = factor_to_base

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.base_units:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.base_units:
            raise ValueError(f"Unknown unit: {to_unit}")

        base_value = value * self.base_units[from_unit]
        result = base_value / self.base_units[to_unit]
        return result

def setup_converter():
    converter = UnitConverter()
    converter.add_unit('meters', 1.0)
    converter.add_unit('kilometers', 1000.0)
    converter.add_unit('centimeters', 0.01)
    converter.add_unit('millimeters', 0.001)
    converter.add_unit('miles', 1609.344)
    converter.add_unit('yards', 0.9144)
    converter.add_unit('feet', 0.3048)
    converter.add_unit('inches', 0.0254)
    return converter

if __name__ == '__main__':
    converter = setup_converter()
    result1 = converter.convert(1, 'meters', 'kilometers')
    print(result1)
    result2 = converter.convert(1, 'miles', 'kilometers')
    print(result2)
    result3 = converter.convert(100, 'centimeters', 'meters')
    print(result3)
    result4 = converter.convert(1, 'inches', 'meters')
    print(result4)
    result5 = converter.convert(5, 'kilometers', 'miles')
    print(result5)