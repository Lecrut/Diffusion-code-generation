class UnitConverter:
    def __init__(self):
        self.base_unit = 'meter'
        self.factors = {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.344
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.factors:
            raise ValueError(f"Unsupported unit: {to_unit}")
        
        value_in_base = value * self.factors[from_unit]
        return value_in_base / self.factors[to_unit]

if __name__ == '__main__':
    converter = UnitConverter()
    result_km_to_m = converter.convert(5.0, 'kilometer', 'meter')
    result_in_to_ft = converter.convert(12.0, 'inch', 'foot')
    result_mi_to_km = converter.convert(1.0, 'mile', 'kilometer')
    print(result_km_to_m)
    print(result_in_to_ft)
    print(result_mi_to_km)