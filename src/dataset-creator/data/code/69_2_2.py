class MassConverter:
    def __init__(self):
        self.constants = {
            'kg': 1.0,
            'g': 0.001,
            'mg': 1e-6,
            'lb': 0.45359237,
            'oz': 0.028349523125,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.constants or to_unit not in self.constants:
            raise ValueError(f"Invalid unit. Supported units are {list(self.constants.keys())}")
        factor = self.constants[from_unit] / self.constants[to_unit]
        return value * factor
if __name__ == '__main__':
    converter = MassConverter()
    sample_tests = [
        (10, 'lb', 'kg'),
        (500, 'g', 'mg'),
        (2.2, 'oz', 'lb')
    ]
    for mass, from_u, to_u in sample_tests:
        result = converter.convert(mass, from_u, to_u)
        print(f"{mass} {from_u} is equal to {result:.6f} {to_u}")