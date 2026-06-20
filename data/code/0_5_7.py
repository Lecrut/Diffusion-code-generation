class UnitConverter:
    def __init__(self, base_unit):
        self.base_unit = base_unit
        self.factors = {}
        self.factors[base_unit] = 1.0

    def add_unit(self, unit, factor_to_base):
        self.factors[unit] = float(factor_to_base)

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unknown unit: {to_unit}")
        base_value = value * self.factors[from_unit]
        return base_value / self.factors[to_unit]

    def get_supported_units(self):
        return list(self.factors.keys())

if __name__ == '__main__':
    converter = UnitConverter('meter')
    converter.add_unit('kilometer', 1000.0)
    converter.add_unit('centimeter', 0.01)
    converter.add_unit('millimeter', 0.001)
    converter.add_unit('inch', 0.0254)
    converter.add_unit('foot', 0.3048)

    result1 = converter.convert(1, 'kilometer', 'meter')
    result2 = converter.convert(100, 'centimeter', 'meter')
    result3 = converter.convert(1, 'meter', 'inch')
    result4 = converter.convert(10, 'foot', 'centimeter')

    print(result1)
    print(result2)
    print(result3)
    print(result4)