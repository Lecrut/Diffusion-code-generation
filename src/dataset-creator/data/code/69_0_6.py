class MassConverter:
    def __init__(self):
        self.si_units = {
            'kg': 1,
            'g': 0.001,
            'mg': 1e-6,
            't': 1000,
        }
        self.cgs_units = {
            'g': 1,
            'mg': 1e-3,
            'kg': 1000,
            'cg': 0.01,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        unit_map = self.si_units.copy()
        unit_map.update(self.cgs_units)
        if from_unit.lower() not in unit_map or to_unit.lower() not in unit_map:
            raise ValueError(f"Unsupported units. Available SI: {list(unit_map.keys())}, CGS: {[k for k in unit_map.keys() if 'g' in str(k).lower()]}")
        base_value = value * unit_map[from_unit.lower()] / unit_map[to_unit.lower()]
        return round(base_value, 6)
if __name__ == '__main__':
    converter = MassConverter()
    result1 = converter.convert(5.0, 'kg', 'g')
    result2 = converter.convert(2e-3, 'mg', 'kg')
    print(f"Converted {result1} grams")
    print(f"Converted {result2} kilograms")