class MassConverter:
    def __init__(self):
        self.si_units = {
            'kilogram': 1,
            'gram': 0.001,
            'milligram': 1e-6,
            'microgram': 1e-9,
            'nanogram': 1e-12
        }
        self.cgs_units = {
            'kilogram': 1,
            'gram': 0.001,
            'milligram': 1e-6,
            'microgram': 1e-9,
            'nanogram': 1e-12
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        unit_map = self.si_units if 'si' in from_unit.lower() else self.cgs_units
        if from_unit not in unit_map or to_unit not in unit_map:
            available_si = list(self.si_units.keys())
            available_cgs = list(self.cgs_units.keys())
            raise ValueError(f"Unsupported units. Available SI: {available_si}, CGS: {available_cgs}")
        factor_from = unit_map[from_unit]
        factor_to = unit_map[to_unit]
        value_in_kg = value * factor_from
        if 'si' in to_unit.lower():
            return value_in_kg / self.si_units.get(to_unit, 1)
        else:
            return value_in_kg / self.cgs_units.get(to_unit, 1)
if __name__ == '__main__':
    converter = MassConverter()
    test_cases = [
        (5000, 'gram', 'kilogram'),
        (2.5, 'milligram', 'microgram'),
        (1e-9, 'nanogram', 'gram'),
        (100, 'kilogram', 'gram')
    ]
    for val, from_u, to_u in test_cases:
        result = converter.convert(val, from_u, to_u)
        print(f"{val} {from_u} -> {result:.6f} {to_u}")