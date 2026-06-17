class MassConverter:
    def __init__(self):
        self.si_units = {
            'kg': 1,
            'g': 0.001,
            'mg': 1e-6,
            'ug': 1e-9,
            't': 1000,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.si_units or to_unit not in self.si_units:
            raise ValueError(f"Unsupported unit. Supported units are {list(self.si_units.keys())}")
        si_value = value * self.si_units[from_unit]
        return si_value / self.si_units[to_unit]
if __name__ == '__main__':
    converter = MassConverter()
    test_cases = [
        (10, 'kg', 'g'),
        (5000, 'mg', 't'),
        (2.5, 'ug', 'kg'),
        (1, 'g', 'mg')
    ]
    for val, from_u, to_u in test_cases:
        result = converter.convert(val, from_u, to_u)
        print(f"{val} {from_u} is equal to {result:.6f} {to_u}")